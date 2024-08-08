#!/usr/bin/python

import os
import sys
import requests
import json
from collections import namedtuple

# set up tests via configuration file
SCRIPT_DIRECTORY = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIRECTORY = os.path.join(os.path.dirname(SCRIPT_DIRECTORY), "config")
CONFIG_FILE = os.getenv("TEST_CONFIG_FILE")
if CONFIG_FILE is not None and CONFIG_FILE.strip() != "":
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, CONFIG_FILE)
    print("test_protein_explorer: using specified configuration file [" + CONFIG_FILE + "]")
else:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, "production.cfg")
    print("test_protein_explorer: configuration file not specified - using default configuration file [" + CONFIG_FILE + "]")
TARGET_WEB_SERVERS = []
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as file_reader:
        mode = None
        for line in file_reader:
            line = line.strip()
            # handle config file sections properly
            normalized_line = line.lower()
            if normalized_line == "[web:massive]":
                mode = "web"
            # unrecognized section for this test suite
            elif line.startswith("["):
                mode = None
            elif mode is not None and mode == "web" and line not in TARGET_WEB_SERVERS:
                TARGET_WEB_SERVERS.append(line)
    print("test_protein_explorer: using test targets from configuration file: web [" + ", ".join(TARGET_WEB_SERVERS) + "]")
else:
    print("test_protein_explorer: configuration file [" + CONFIG_FILE + "] is not present - using default test targets: web [massive.ucsd.edu]")
    TARGET_WEB_SERVERS.append("massive.ucsd.edu")

URLTest = namedtuple('URLTest', 'url, exp, parse_func, result_func, failure_message')

test_list = {
    'Protein count with 1+ unique peptides in MassIVE-KB (incl synthetics)': URLTest(
        url = 'https://' + TARGET_WEB_SERVERS[0] + '/ProteoSAFe/ProteinLibraryServlet?task=protein_explorer_proteins&file=&pageSize=30&offset=0&query=%2523%257B%2522unroll%2522%253A%2522no%2522%252C%2522include_synthetics%2522%253A%2522yes%2522%252C%2522globalpeptides_lowerinput%2522%253A%25221%2522%257D&query_type=representative&_=1570576288527',
        exp = 19550,
        parse_func = lambda x: x['total_rows'],
        result_func = lambda x, y: x == y,
        failure_message = lambda x, y: 'Expected {} proteins, instead found {}'.format(x,y)
    ),
    'Protein count with 1+ HUPO peptides in MassIVE-KB (incl synthetics)': URLTest(
        url = 'https://' + TARGET_WEB_SERVERS[0] + '/ProteoSAFe/ProteinLibraryServlet?task=protein_explorer_proteins&file=&pageSize=30&offset=0&query=%2523%257B%2522unroll%2522%253A%2522no%2522%252C%2522include_synthetics%2522%253A%2522yes%2522%252C%2522globalnonoverlapping_lowerinput%2522%253A%25221%2522%257D&query_type=representative&_=1570576288529',
        exp = 19154,
        parse_func = lambda x: x['total_rows'],
        result_func = lambda x, y: x == y,
        failure_message = lambda x, y: 'Expected {} proteins, instead found {}'.format(x,y)
    )
}

def test_call(test_key):
    url, exp, parse_func, result_func, failure_message = test_list[test_key]
    req = requests.get(url)
    assert(req.status_code == 200, "Status code incorrect")
    res = parse_func(req.json())
    assert(result_func(res, exp), failure_message(exp, res))

def test_generator():
    for test in test_list.keys():
        yield test_call, test

def test_protein_explorer_proteins():
    for target in TARGET_WEB_SERVERS:
        # proteins
        url = "https://" + target + "/ProteoSAFe/ProteinLibraryServlet?task=protein_explorer_proteins&file=&pageSize=30&offset=0&query=%2523%257B%2522unroll%2522%253A%2522no%2522%252C%2522include_synthetics%2522%253A%2522yes%2522%252C%2522datasets%2522%253A%2522%2522%252C%2522accession_input%2522%253A%2522%2522%252C%2522peptides_input%2522%253Anull%257D&query_type=representative"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PeptideExplorer")
        assert(len(content["row_data"]) == 30)
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content["row_data"][0]["accession"]
        content["row_data"][0]["description"]
        content["row_data"][0]["gene"]
        content["row_data"][0]["proteinexistance"]
        content["row_data"][0]["globalpeptides"]
        content["row_data"][0]["globalnonoverlapping"]
        content["row_data"][0]["globalexonunique"]
        content["row_data"][0]["globalpsmsshared"]
        content["row_data"][0]["globalpsmsunique"]
        response.raise_for_status()

def test_protein_explorer_annotations():
    for target in TARGET_WEB_SERVERS:
        # protein annotation
        url = "https://" + target + "/ProteoSAFe/ProteinAnnotationServlet?protein_name=O00203"
        response = requests.get(url, timeout=10)
        content = response.json()
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content["accession"]
        content["description"]
        content["gene"]
        content["sequence_il"]
        content["uniprot_pe"]
        content["nextprot_pe"]
        content["annotations_rendered"]
        response.raise_for_status()

def test_protein_explorer_libraries():
    for target in TARGET_WEB_SERVERS:
        # peptide libraries
        url = "https://" + target + "/ProteoSAFe/PeptideLibraryServlet"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(len(content) >= 7)
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content[0]["library_id"]
        content[0]["name"]
        content[0]["version"]
        content[0]["dataset_id"]
        content[0]["active"]
        response.raise_for_status()


def test_protein_explorer_map():
    for target in TARGET_WEB_SERVERS:
        # protein coverage map
        url = "https://" + target + "/ProteoSAFe/ProteinCoverageServlet?query_type=Map&protein_name=O00203&libraries=1,2&query=%257B%2522overlaps%2522%253Afalse%252C%2522libraries%2522%253A%25221%252C2%2522%252C%2522protein_name%2522%253A%2522O00203%2522%257D"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PeptideExplorer")
        assert(len(content["row_data"]) == content["total_rows"])
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content["row_data"][0]["library"]
        content["row_data"][0]["variant"]
        content["row_data"][0]["spectra"]
        content["row_data"][0]["start_aa"]
        content["row_data"][0]["end_aa"]
        response.raise_for_status()

def test_protein_explorer_representatives():
    for target in TARGET_WEB_SERVERS:
        # representatives
        url = "https://" + target + "/ProteoSAFe/ProteinCoverageServlet?task=protein_explorer_representatives&file=&pageSize=10&offset=0&query=%2523%257B%2522overlaps%2522%253Afalse%252C%2522libraries%2522%253A%25221%252C2%2522%252C%2522protein_name%2522%253A%2522O00203%2522%257D&query_type=representative&_=1677257072853"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PeptideExplorer")
        assert(len(content["row_data"]) == 10)
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content["row_data"][0]["library"]
        content["row_data"][0]["sequence"]
        content["row_data"][0]["length"]
        content["row_data"][0]["mapped"]
        content["row_data"][0]["overlapping"]
        content["row_data"][0]["exonunique"]
        content["row_data"][0]["exonjunction"]
        content["row_data"][0]["spectra"]
        content["row_data"][0]["samples"]
        content["row_data"][0]["occurances"]
        content["row_data"][0]["startaa"]
        content["row_data"][0]["endaa"]
        response.raise_for_status()

def test_protein_explorer_provenance():
    for target in TARGET_WEB_SERVERS:
        # provenance
        url = "https://" + target + "/ProteoSAFe/ProteinCoverageServlet?task=protein_explorer_provenance&file=&pageSize=10&offset=0&query=%2523%257B%2522overlaps%2522%253Afalse%252C%2522libraries%2522%253A%25221%252C2%2522%252C%2522protein_name%2522%253A%2522O00203%2522%257D&query_type=provenance&_=1677257072854"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PeptideExplorer")
        assert(len(content["row_data"]) == 10)
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content["row_data"][0]["library"]
        content["row_data"][0]["sequence"]
        content["row_data"][0]["dataset"]
        content["row_data"][0]["filename"]
        content["row_data"][0]["nativeid"]
        content["row_data"][0]["charge"]
        content["row_data"][0]["search"]
        response.raise_for_status()
