#!/usr/bin/python


import sys
import getopt
import os
import requests

import os

def test_ms2lda_motifdb():
    server_url = 'https://ms2lda.org/motifdb/'

    print('Grabbing the latest Motifs from MS2LDA')
    motifset_dict = requests.get(server_url + 'list_motifsets/').json()

    db_list = []
    db_list.append(2)
    db_list.append(4)
    db_list.append(1)
    db_list.append(3)
    db_list.append(5)
    db_list.append(6)
    db_list.append(16)

    data = {}
    data['motifset_id_list'] = db_list
    data['filter'] = 'True'

    print('Getting motifsets')
    response = requests.post(server_url + 'get_motifset/', data=data)
    json_output = response.json()

    assert len(motifset_dict) > 0
    assert response.status_code == 200
    assert len(json_output['motifs']) > 0
    assert len(json_output['metadata']) > 0