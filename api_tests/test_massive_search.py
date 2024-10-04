import requests

def test_search_loadtime():
    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522psms%2522%257D&query_type=psm&_=1489704532486"
    response = requests.get(url, timeout=60)
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

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522peptides%2522%257D&query_type=peptide&_=1489704532487"
    response = requests.get(url, timeout=60)
    content = response.json()
    assert(content["source"] == "PROXI")
    assert(len(content["row_data"]) == 30)
    content["row_data"][0]["sequence"]
    response.raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522variants%2522%257D&query_type=variant&_=1489704532488"
    response = requests.get(url, timeout=60)
    content = response.json()
    assert(content["source"] == "PROXI")
    assert(len(content["row_data"]) == 30)
    content["row_data"][0]["sequence"]
    content["row_data"][0]["charge"]
    content["row_data"][0]["peptide_id"]
    response.raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522proteins%2522%257D&query_type=protein&_=1489704532490"
    response = requests.get(url, timeout=60)
    content = response.json()
    assert(content["source"] == "PROXI")
    assert(len(content["row_data"]) == 30)
    content["row_data"][0]["name"]
    response.raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522ptms%2522%257D&query_type=modification&_=1489704532489"
    response = requests.get(url, timeout=60)
    content = response.json()
    assert(content["source"] == "PROXI")
    assert(len(content["row_data"]) == 30)
    content["row_data"][0]["name"]
    content["row_data"][0]["mass"]
    response.raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522mztabs%2522%257D&query_type=mztab&_=1489704532491"
    response = requests.get(url, timeout=60)
    content = response.json()
    assert(content["source"] == "PROXI")
    assert(len(content["row_data"]) == 30)
    content["row_data"][0]["dataset_id"]
    content["row_data"][0]["file_descriptor"]
    response.raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522peptides%2522%252C%2522table_sort_history%2522%253A%2522variant_sequence_dsc%253Bsequence_dsc%2522%257D&query_type=peptide&_=1489704532502"
    response = requests.get(url, timeout=60)
    content = response.json()
    assert(content["source"] == "PROXI")
    assert(len(content["row_data"]) == 30)
    # verify that peptides are correctly sorted in descending order; first sequence should start with "Z"
    assert(content["row_data"][0]["sequence"].startswith("Z"))
    response.raise_for_status()

