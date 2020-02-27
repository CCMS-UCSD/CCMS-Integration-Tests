import requests


def test_search_loadtime():
    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522psms%2522%257D&query_type=psm&_=1489704532486"
    requests.get(url, timeout=10).raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522peptides%2522%257D&query_type=peptide&_=1489704532487"
    requests.get(url, timeout=20).raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522variants%2522%257D&query_type=variant&_=1489704532488"
    requests.get(url, timeout=20).raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522ptms%2522%257D&query_type=modification&_=1489704532489"
    requests.get(url, timeout=10).raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522proteins%2522%257D&query_type=protein&_=1489704532490"
    requests.get(url, timeout=10).raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522mztabs%2522%257D&query_type=mztab&_=1489704532491"
    requests.get(url, timeout=10).raise_for_status()

    url = "http://massive.ucsd.edu/ProteoSAFe/QueryPROXI?task=N%2FA&file=&pageSize=30&offset=0&query=%2523%257B%2522searched_button%2522%253A%2522peptides%2522%252C%2522table_sort_history%2522%253A%2522variant_sequence_dsc%253Bsequence_dsc%2522%257D&query_type=peptide&_=1489704532502"
    requests.get(url, timeout=20).raise_for_status()

