#!/usr/bin/python

import sys
import requests
import json
from collections import namedtuple

URLTest = namedtuple('URLTest', 'url, exp, parse_func, result_func, failure_message')

test_list = {
    'Protein count with 1+ unique peptides in MassIVE-KB (incl synthetics)': URLTest(
        url = 'https://massive.ucsd.edu/ProteoSAFe/ProteinLibraryServlet?task=protein_explorer_proteins&file=&pageSize=30&offset=0&query=%2523%257B%2522unroll%2522%253A%2522no%2522%252C%2522include_synthetics%2522%253A%2522yes%2522%252C%2522globalpeptides_lowerinput%2522%253A%25221%2522%257D&query_type=representative&_=1570576288527',
        exp = 19550,
        parse_func = lambda x: x['total_rows'],
        result_func = lambda x, y: x == y,
        failure_message = lambda x, y: 'Expected {} proteins, instead found {}'.format(x,y)
    ),
    'Protein count with 1+ HUPO peptides in MassIVE-KB (incl synthetics)': URLTest(
        url = 'https://massive.ucsd.edu/ProteoSAFe/ProteinLibraryServlet?task=protein_explorer_proteins&file=&pageSize=30&offset=0&query=%2523%257B%2522unroll%2522%253A%2522no%2522%252C%2522include_synthetics%2522%253A%2522yes%2522%252C%2522globalnonoverlapping_lowerinput%2522%253A%25221%2522%257D&query_type=representative&_=1570576288529',
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

def test_protein_explorer_apis():
    # proteins
    url = "https://massive.ucsd.edu/ProteoSAFe/ProteinLibraryServlet?task=protein_explorer_proteins&file=&pageSize=30&offset=0&query=%2523%257B%2522unroll%2522%253A%2522no%2522%252C%2522include_synthetics%2522%253A%2522yes%2522%252C%2522datasets%2522%253A%2522%2522%252C%2522accession_input%2522%253A%2522%2522%252C%2522peptides_input%2522%253Anull%257D&query_type=representative"
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

    # protein annotation
    url = "https://massive.ucsd.edu/ProteoSAFe/ProteinAnnotationServlet?protein_name=O00203"
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

    # peptide libraries
    url = "https://massive.ucsd.edu/ProteoSAFe/PeptideLibraryServlet"
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

    # protein coverage map
    url = "https://massive.ucsd.edu/ProteoSAFe/ProteinCoverageServlet?query_type=Map&protein_name=O00203&libraries=1,2&query=%257B%2522overlaps%2522%253Afalse%252C%2522libraries%2522%253A%25221%252C2%2522%252C%2522protein_name%2522%253A%2522O00203%2522%257D"
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

    # representatives
    url = "https://massive.ucsd.edu/ProteoSAFe/ProteinCoverageServlet?task=protein_explorer_representatives&file=&pageSize=10&offset=0&query=%2523%257B%2522overlaps%2522%253Afalse%252C%2522libraries%2522%253A%25221%252C2%2522%252C%2522protein_name%2522%253A%2522O00203%2522%257D&query_type=representative&_=1677257072853"
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

    # provenance
    url = "https://massive.ucsd.edu/ProteoSAFe/ProteinCoverageServlet?task=protein_explorer_provenance&file=&pageSize=10&offset=0&query=%2523%257B%2522overlaps%2522%253Afalse%252C%2522libraries%2522%253A%25221%252C2%2522%252C%2522protein_name%2522%253A%2522O00203%2522%257D&query_type=provenance&_=1677257072854"
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
