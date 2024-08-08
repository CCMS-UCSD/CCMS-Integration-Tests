import os
import requests

# set up tests via configuration file
SCRIPT_DIRECTORY = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIRECTORY = os.path.join(os.path.dirname(SCRIPT_DIRECTORY), "config")
CONFIG_FILE = os.getenv("TEST_CONFIG_FILE")
if CONFIG_FILE is not None:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, CONFIG_FILE)
    print("test_massive_search: using specified configuration file [" + CONFIG_FILE + "]")
else:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, "production.cfg")
    print("test_massive_search: configuration file not specified - using default configuration file [" + CONFIG_FILE + "]")
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
            elif mode is not None and mode == "web":
                TARGET_WEB_SERVERS.append(line)
    print("test_massive_search: using test targets from configuration file: web [" + ", ".join(TARGET_WEB_SERVERS) + "]")
else:
    print("test_massive_search: configuration file [" + CONFIG_FILE + "] is not present - using default test targets: web [massive.ucsd.edu]")
    TARGET_WEB_SERVERS.append("massive.ucsd.edu")

def test_search_loadtime():
    for target in TARGET_WEB_SERVERS:
        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522psms%2522%257D&query_type=psm&_=1489704532486"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        # verify that expected keys are present; simply dereferencing will throw a KeyError if the key is missing
        content["row_data"][0]["dataset_id"]
        content["row_data"][0]["resultfile_id"]
        content["row_data"][0]["id_in_file"]
        content["row_data"][0]["spectrumfile_id"]
        content["row_data"][0]["nativeid"]
        content["row_data"][0]["peptide_id"]
        content["row_data"][0]["variant_id"]
        response.raise_for_status()

        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522peptides%2522%257D&query_type=peptide&_=1489704532487"
        response = requests.get(url, timeout=20)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        content["row_data"][0]["sequence"]
        response.raise_for_status()

        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522variants%2522%257D&query_type=variant&_=1489704532488"
        response = requests.get(url, timeout=30)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        content["row_data"][0]["sequence"]
        content["row_data"][0]["charge"]
        content["row_data"][0]["peptide_id"]
        response.raise_for_status()

        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522proteins%2522%257D&query_type=protein&_=1489704532490"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        content["row_data"][0]["name"]
        response.raise_for_status()

        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522ptms%2522%257D&query_type=modification&_=1489704532489"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        content["row_data"][0]["name"]
        content["row_data"][0]["mass"]
        response.raise_for_status()

        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522mztabs%2522%257D&query_type=mztab&_=1489704532491"
        response = requests.get(url, timeout=10)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        content["row_data"][0]["dataset_id"]
        content["row_data"][0]["file_descriptor"]
        response.raise_for_status()

        url = "http://" + target + "/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522peptides%2522%252C%2522table_sort_history%2522%253A%2522variant_sequence_dsc%253Bsequence_dsc%2522%257D&query_type=peptide&_=1489704532502"
        response = requests.get(url, timeout=20)
        content = response.json()
        assert(content["source"] == "PROXI")
        assert(len(content["row_data"]) == 30)
        # verify that peptides are correctly sorted in descending order; first sequence should start with "Z"
        assert(content["row_data"][0]["sequence"].startswith("Z"))
        response.raise_for_status()
