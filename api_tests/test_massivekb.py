#!/usr/bin/python


import sys
import getopt
import os
import requests

import os


def get_status(search_task_object):
    status = "OK"
    try:
        search_task_url = "https://proteomics2.ucsd.edu/ProteoSAFe/result_json.jsp?task=%s&view=view_result_list" % (search_task_object["search_task_id"])
        mztab_summary_list = requests.get(search_task_url).json()["blockData"]
        file_descriptor = mztab_summary_list[0]["File_descriptor"]
        psms_url = "https://proteomics2.ucsd.edu/ProteoSAFe/result_json.jsp?task=%s&view=group_by_spectrum&file=%s" % (search_task_object["search_task_id"], file_descriptor)

        psms_object = requests.get(psms_url).json()
        number_of_rows = int(psms_object["blockData"]["total_rows"])
        if number_of_rows < 1:
            status = "ERROR" + " " + search_task_object["search_task_id"]
        else:
            status = "OK" + " " + search_task_object["search_task_id"]
    except KeyboardInterrupt:
        raise
    except:
        status = "ERROR" + " " + search_task_object["search_task_id"]

    #print(status)

    return status

def test_provenance():
    #massive_kb_library_task = "3cac03860ff7453a821332ab4cff20f4" #Primary Library
    massive_kb_library_task = "e33a302ea7e94422bf2b122260d22cc6" #No synthetics
    #massive_kb_library_task = "86798dfb8f194d708394b3dd6ed6124b" #Only synthetics

    all_search_kb_url = "https://massive.ucsd.edu/ProteoSAFe/result_json.jsp?task=%s&view=view_all_search_tasks" % (massive_kb_library_task)
    filename = requests.get(all_search_kb_url).json()["blockData"]["file"]
    full_query = "https://massive.ucsd.edu/ProteoSAFe/QueryResult?task=%s&file=%s&pageSize=0&offset=0&query=&totalRows=7495&_=1525380968458" % (massive_kb_library_task, filename)
    all_search_tasks = requests.get(full_query).json()["row_data"]

    #Subsampling the provenance
    all_search_tasks = all_search_tasks[:100]

    all_statuses = []
    for search_task in all_search_tasks:
        status = get_status(search_task)
        all_statuses.append(status)

    all_error_statuses = [status for status in all_statuses if status.find("ERROR") != -1]
    print("Number of Errors", len(all_error_statuses))

    assert(len(all_error_statuses) > 5, "Too Many Provenance Failures")

def test_massive_kb():
    #Datasets Page
    requests.get("http://massive.ucsd.edu/ProteoSAFe/static/massive-kb-libraries.jsp", timeout=10).raise_for_status()

    #all library variants
    requests.get("http://massive.ucsd.edu/ProteoSAFe/result.jsp?task=e1d143d146fc4045aea48e2a7044e4d9&view=ambiguity_library_view_split", timeout=10).raise_for_status()

    #search provenance
    requests.get("http://massive.ucsd.edu/ProteoSAFe/result.jsp?task=e1d143d146fc4045aea48e2a7044e4d9&view=view_all_search_tasks", timeout=10).raise_for_status()

    #Proteins
    requests.get("http://massive.ucsd.edu/ProteoSAFe/result.jsp?task=e1d143d146fc4045aea48e2a7044e4d9&view=protein_list", timeout=10).raise_for_status()
