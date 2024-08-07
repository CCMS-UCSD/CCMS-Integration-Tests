import os
import requests

# set up test via configuration file
SCRIPT_DIRECTORY = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIRECTORY = os.path.join(os.path.dirname(SCRIPT_DIRECTORY), "config")
CONFIG_FILE = os.getenv("TEST_CONFIG_FILE")
if CONFIG_FILE is not None:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, CONFIG_FILE)
    print("Using specified configuration file [" + CONFIG_FILE + "]")
else:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, "massive.cfg")
    print("Configuration file not specified - using default configuration file [" + CONFIG_FILE + "]")
TEST_TARGETS = []
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as file_reader:
        for line in file_reader:
            TEST_TARGETS.append(line.strip())
    print("Using test targets from configuration file: [" + ", ".join(TEST_TARGETS) + "]")
else:
    print("Configuration file [" + CONFIG_FILE + "] is not present - using default test target \"massive.ucsd.edu\"")
    TEST_TARGETS.append("massive.ucsd.edu")

def test_massive_apis():
    for target in TEST_TARGETS:
        url = "https://" + target + "/ProteoSAFe/proxi/v0.1/datasets?filter=MSV000084741&function=datasets"
        r = requests.get(url, timeout=5)
        r.raise_for_status()

def test_massive_usi_resolution():
    for target in TEST_TARGETS:
        url = "https://" + target + "/ProteoSAFe/QuerySpectrum?id=mzspec:MSV000085852:QC_0:scan:1"
        r = requests.get(url, timeout=5)
        r.raise_for_status()

def test_massive_webpage():
    for target in TEST_TARGETS:
        requests.get("http://" + target + "/ProteoSAFe/datasets.jsp", timeout=10).raise_for_status() #Datasets Page
        requests.get("http://" + target + "/ProteoSAFe/dataset.jsp?task=fd246a746e0749c5ad0403be265bb2ea", timeout=10).raise_for_status() #Dataset Page
        requests.get("http://" + target + "/ProteoSAFe/MassiveServlet?function=reanalysis&task=fd246a746e0749c5ad0403be265bb2ea", timeout=10).raise_for_status() #Reanalysese
        requests.get("http://" + target + "/ProteoSAFe/MassiveServlet?function=massivehistory&massiveid=MSV000079514", timeout=10).raise_for_status()
        # Jeremy 3/22/23: increasing timeout for the "massivesummary" API call, since the query is slower than anticipated;
        # need to figure out exactly why it's so slow and fix it, but for now it's okay if it takes a bit longer
        requests.get("http://" + target + "/ProteoSAFe/MassiveServlet?function=massivesummary&massiveid=MSV000079514", timeout=30).raise_for_status()

def test_massive_ftp():
    import urllib.request
    for target in TEST_TARGETS:
        url = "ftp://" + target + "/v01/MSV000080469"
        print(url)
        urllib.request.urlopen(url)
        url = "ftp://" + target + "/v01/MSV000079146"
        print(url)
        urllib.request.urlopen(url)
        url = "ftp://" + target + "/v01/MSV000079339"
        print(url)
        urllib.request.urlopen(url)
        url = "ftp://" + target + "/v01/MSV000079341"
        print(url)
        urllib.request.urlopen(url)
        url = "ftp://" + target + "/v01/MSV000079344"
        print(url)
        urllib.request.urlopen(url)
        url = "ftp://" + target + "/v01/MSV000080469/peak/AMG_mzXML/10317.000006947.mzXML"
        print(url)
        urllib.request.urlopen(url)

def msstats_annotation_servlet():
    for target in TEST_TARGETS:
        url = "https://" + target + "/ProteoSAFe/MSStatsAnnotationServlet?filepath=f.benpullman%2FMSV000080025_mplex_calu3_MERS_CoV_response.csv%3B&header=Condition"
        r = requests.get(url)
        r.raise_for_status()
        url ="https://" + target + "/ProteoSAFe/MSStatsAnnotationServlet?filepath=f.benpullman%2FMSV000080025_mplex_calu3_MERS_CoV_response.csv%3B&header=Missing"
        r = requests.get(url)
        assert(r.status_code == 400)

def test_massive_usi():
    for target in TEST_TARGETS:
        url = "https://" + target + "/ProteoSAFe/QuerySpectrum?id=mzspec%3ARMSV000000308.2%3Apeak%2Fspecs_ms.mgf%3Aindex%3A262144%3A%5B229.162932%5D-EMEAELEDERK%5B229.163%5D&_=1588805688884"
        r = requests.get(url)
        r.raise_for_status()
        assert("f.RMSV" in r.json()["row_data"][0]["file_descriptor"])

def test_massive_task_usi_resolution():
    for target in TEST_TARGETS:
        url = "https://" + target + "/ProteoSAFe/QuerySpectrum?id=mzspec:MassIVE:TASK-f4b86b150a164ee4a440b661e97a7193-spectra:scan:471429"
        r = requests.get(url)
        r.raise_for_status()
