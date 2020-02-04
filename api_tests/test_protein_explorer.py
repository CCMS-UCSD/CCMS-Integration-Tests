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
    assert(result_func(res, exp), failure_message(res,exp))

def test_generator():
    for test in test_list.keys():
        yield test_call, test
