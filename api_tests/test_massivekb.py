#!/usr/bin/python

import sys
import getopt
import os
import requests

# set up tests via configuration file
SCRIPT_DIRECTORY = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIRECTORY = os.path.join(os.path.dirname(SCRIPT_DIRECTORY), "config")
CONFIG_FILE = os.getenv("TEST_CONFIG_FILE")
if CONFIG_FILE is not None and CONFIG_FILE.strip() != "":
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, CONFIG_FILE)
    print("test_massivekb: using specified configuration file [" + CONFIG_FILE + "]")
else:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, "production.cfg")
    print("test_massivekb: configuration file not specified - using default configuration file [" + CONFIG_FILE + "]")
TARGET_WEB_SERVERS = []
TASK_QUERY_WEB_SERVER = None
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as file_reader:
        mode = None
        for line in file_reader:
            line = line.strip()
            # handle config file sections properly
            normalized_line = line.lower()
            if normalized_line == "[web:massive]":
                mode = "web"
            elif normalized_line == "[web:task_query]":
                mode = "task"
            # unrecognized section for this test suite
            elif line.startswith("["):
                mode = None
            elif mode is not None:
                if mode == "web" and line not in TARGET_WEB_SERVERS:
                    TARGET_WEB_SERVERS.append(line)
                elif mode == "task" and TASK_QUERY_WEB_SERVER is None:
                    TASK_QUERY_WEB_SERVER = line
    print("test_massivekb: using test targets from configuration file: web [" + ", ".join(TARGET_WEB_SERVERS) + "] / task query [" + TASK_QUERY_WEB_SERVER + "]")
else:
    print("test_massivekb: configuration file [" + CONFIG_FILE + "] is not present - using default test targets: web [massive.ucsd.edu] / task query [proteomics2.ucsd.edu]")
    TARGET_WEB_SERVERS.append("massive.ucsd.edu")
    TASK_QUERY_WEB_SERVER = "proteomics2.ucsd.edu"

def get_status(search_task_object):
    status = "OK"
    try:
        search_task_url = "https://" + TASK_QUERY_WEB_SERVER + "/ProteoSAFe/result_json.jsp?task=%s&view=view_result_list" % (search_task_object["search_task_id"])
        mztab_summary_list = requests.get(search_task_url).json()["blockData"]
        file_descriptor = mztab_summary_list[0]["File_descriptor"]
        psms_url = "https://" + TASK_QUERY_WEB_SERVER + "/ProteoSAFe/result_json.jsp?task=%s&view=group_by_spectrum&file=%s" % (search_task_object["search_task_id"], file_descriptor)

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
    for target in TARGET_WEB_SERVERS:
        #massive_kb_library_task = "3cac03860ff7453a821332ab4cff20f4" #Primary Library
        massive_kb_library_task = "e33a302ea7e94422bf2b122260d22cc6" #No synthetics
        #massive_kb_library_task = "86798dfb8f194d708394b3dd6ed6124b" #Only synthetics
        all_search_kb_url = "https://" + target + "/ProteoSAFe/result_json.jsp?task=%s&view=view_all_search_tasks" % (massive_kb_library_task)
        filename = requests.get(all_search_kb_url).json()["blockData"]["file"]
        full_query = "https://" + target + "/ProteoSAFe/QueryResult?task=%s&file=%s&pageSize=0&offset=0&query=&totalRows=7495&_=1525380968458" % (massive_kb_library_task, filename)
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
    for target in TARGET_WEB_SERVERS:
        #Datasets Page
        requests.get("http://" + target + "/ProteoSAFe/static/massive-kb-libraries.jsp", timeout=10).raise_for_status()
        #all library variants
        requests.get("http://" + target + "/ProteoSAFe/result.jsp?task=e1d143d146fc4045aea48e2a7044e4d9&view=ambiguity_library_view_split", timeout=10).raise_for_status()
        #search provenance
        requests.get("http://" + target + "/ProteoSAFe/result.jsp?task=e1d143d146fc4045aea48e2a7044e4d9&view=view_all_search_tasks", timeout=10).raise_for_status()
        #Proteins
        requests.get("http://" + target + "/ProteoSAFe/result.jsp?task=e1d143d146fc4045aea48e2a7044e4d9&view=protein_list", timeout=10).raise_for_status()
