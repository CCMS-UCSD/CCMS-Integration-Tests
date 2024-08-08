import requests
import json
import zipfile
import os

# set up tests via configuration file
SCRIPT_DIRECTORY = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_DIRECTORY = os.path.join(os.path.dirname(SCRIPT_DIRECTORY), "config")
CONFIG_FILE = os.getenv("TEST_CONFIG_FILE")
if CONFIG_FILE is not None and CONFIG_FILE.strip() != "":
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, CONFIG_FILE)
    print("test_gnps_api: using specified configuration file [" + CONFIG_FILE + "]")
else:
    CONFIG_FILE = os.path.join(CONFIG_DIRECTORY, "production.cfg")
    print("test_gnps_api: configuration file not specified - using default configuration file [" + CONFIG_FILE + "]")
TARGET_WEB_SERVERS = []
TARGET_FTP_SERVERS = []
if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as file_reader:
        mode = None
        for line in file_reader:
            line = line.strip()
            # handle config file sections properly
            normalized_line = line.lower()
            if normalized_line == "[web:gnps]":
                mode = "web"
            elif normalized_line == "[ftp:gnps]":
                mode = "ftp"
            # unrecognized section for this test suite
            elif line.startswith("["):
                mode = None
            elif mode is not None:
                if mode == "web":
                    TARGET_WEB_SERVERS.append(line)
                elif mode == "ftp":
                    TARGET_FTP_SERVERS.append(line)
    print("test_gnps_api: using test targets from configuration file: web [" + ", ".join(TARGET_WEB_SERVERS) + "] / FTP [" + ", ".join(TARGET_FTP_SERVERS) + "]")
else:
    print("test_gnps_api: configuration file [" + CONFIG_FILE + "] is not present - using default test targets: web [gnps.ucsd.edu] / FTP [ccms-ftp.ucsd.edu]")
    TARGET_WEB_SERVERS.append("gnps.ucsd.edu")
    TARGET_FTP_SERVERS.append("ccms-ftp.ucsd.edu")

def test_continuous_id():
    for target in TARGET_WEB_SERVERS:
        url = "https://" + target + "/ProteoSAFe/ContinuousIDServlet?task=ee21d1b9bca04a908d231e4048e6a14a"
        data = requests.get(url)
        continuous_id_object = json.loads(data.text)
        jobs = continuous_id_object["jobs"]
        assert(len(jobs) > 10)
        #Testing a specific continuous ID
        url = "https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=e00e4bc53e8240389deaa68596ca8eaa&view=group_by_spectrum_all_beta"
        data = requests.get(url)
        all_identifications_list = json.loads(data.text)["blockData"]
        assert(len(all_identifications_list) > 50)


def test_datasets():
    for target in TARGET_WEB_SERVERS:
        url = "https://" + target + "/ProteoSAFe/datasets_json.jsp"
        data = requests.get(url)
        datasets = json.loads(data.text)
        datasets_list = datasets["datasets"]
        assert(len(datasets_list) > 500)
        #testing to make sure the massive servlet works for all GNPS datasets
        for dataset in datasets_list[:50]:
            if "GNPS" in dataset["title"].upper():
                task_id = dataset["task"]
                #print(dataset["title"].encode(encoding="ascii", errors="ignore"))
                url = "https://" + target + "/ProteoSAFe/MassiveServlet?task={}&function=massiveinformation&_=1563563757014".format(task_id)
                r = requests.get(url)
                try:
                    r.raise_for_status()
                except KeyboardInterrupt:
                    raise
                except:
                    print(url)
                    raise

def test_dataset_api():
    for target in TARGET_WEB_SERVERS:
        url = "https://" + target + "/ProteoSAFe/QueryDatasets?task=N%2FA&file=&pageSize=30&offset=0&query=%257B%2522query%2522%253A%257B%257D%252C%2522table_sort_history%2522%253A%2522createdMillis_dsc%2522%252C%2522title_input%2522%253A%2522GNPS%2522%257D&target=&_=1583795399976"
        r = requests.get(url)
        r.raise_for_status()


def test_direct_download():
    for target in TARGET_WEB_SERVERS:
        test_urls = []
        test_urls.append("https://" + target + "/ProteoSAFe/DownloadResultFile?task=3fdc6adc5c104652a78caf70d513c8c3&block=main&file=output_graphml/")
        test_urls.append("https://" + target + "/ProteoSAFe/DownloadResultFile?task=047ef85223024f269e44492adc771d9c&block=main&file=gnps_molecular_network_graphml/")
        test_urls.append("http://" + target + "/ProteoSAFe/DownloadResultFile?task=ddd650381cef4bcfad4b068e9400c8d7&block=main&file=f.MSV000085444/ccms_peak/peak/Hui_N1_fe.mzML")
        test_urls.append("http://" + target + "/ProteoSAFe/DownloadResultFile?task=ddd650381cef4bcfad4b068e9400c8d7&block=main&file=f.mwang87/data/Metabolomics/Cheese/mzML/09.mzML")
        for url in test_urls:
            print(url)
            r = requests.get(url)
            assert(r.status_code == 200)
            assert(len(r.text) > 50000)
        test_urls = []
        test_urls.append("https://" + target + "/ProteoSAFe/DownloadResultFile?task=45c638496d9942e5a855fa051b63701d&file=written_description/0b04a5972a074141a442238ab3448049.html&block=main")
        for url in test_urls:
            print(url)
            r = requests.get(url)
            assert(r.status_code == 200)

def test_download_result_zip():
    task_id = "047ef85223024f269e44492adc771d9c"
    for target in TARGET_WEB_SERVERS:
        url_to_zip = "https://" + target + "/ProteoSAFe/DownloadResult?task={}&show=true&view=download_cytoscape_data".format(task_id)
        r = requests.post(url_to_zip)
        zip_filename = os.path.join(".", "%s.zip" % (task_id))
        with open(zip_filename, "wb") as local_file:
            local_file.write(r.content)
        from zipfile import ZipFile
        with ZipFile(zip_filename, 'r') as zipObj:
            listOfFileNames = zipObj.namelist()
            assert(len(listOfFileNames) >= 5)
        os.remove(zip_filename)

def test_gnps_library():
    import utils
    for target in TARGET_WEB_SERVERS:
        url = "https://" + target + "/ProteoSAFe/gnpslibrary.jsp?library=GNPS-LIBRARY&test=true"
        r = requests.get(url)
        assert(len(r.text) > 20000)
        url = "https://" + target + "/ProteoSAFe/SpectrumCommentServlet?SpectrumID=CCMSLIB00000001547"
        utils.test_load_time(url, 20000)
        r = requests.get(url)
        assert(len(r.json()["spectruminfo"]["peaks_json"]) > 100)
        url = "https://" + target + "/ProteoSAFe/static/gnps-splash.jsp?test=true"
        utils.test_load_time(url, 20000)
        url = "https://" + target + "/ProteoSAFe/gnpslibrary.jsp?library=GNPS-LIBRARY&test=true#%7B%22Library_Class_input%22%3A%221%7C%7C2%7C%7C3%7C%7CEXACT%22%7D"
        utils.test_load_time(url, 20000)
        url = "https://" + target + "/ProteoSAFe/ContinuousIDRatingSummaryServlet?spectrum_id=CCMSLIB00000006885&summary_type=per_spectrum"
        data = requests.get(url)
        ratings_list = json.loads(data.text)["ratings"]
        assert(len(ratings_list) > 1)
        url = "https://" + target + "/ProteoSAFe/ContinuousIDRatingSummaryServlet?dataset_id=MSV000078547&summary_type=per_dataset"
        data =  requests.get(url)
        ratings_list = json.loads(data.text)["ratings"]
        assert(len(ratings_list) > 1)

def test_gnps_library_provenance():
    import urllib.request
    for target in TARGET_FTP_SERVERS:
        url = "ftp://" + target + "/GNPS_Library_Provenance/47daa4396adb426eaa5fa54b6ce7dd5f/130618_Ger_Jenia_WT-3-Des-MCLR_MH981.4-qb.1.1..mgf"
        print(url)
        response = urllib.request.urlopen(url)
        html = response.read()
        assert(len(html) == 4615)

def test_gnps_network_views():
    for target in TARGET_WEB_SERVERS:
        url = "https://" + target + "/ProteoSAFe/result_json.jsp?task=d0e3af94f33f47acad56560de0c5a846&view=view_all_annotations_DB"
        data = requests.get(url)
        identication_data = json.loads(data.text)["blockData"]
        assert(len(identication_data) == 204)
        url = "https://" + target + "/ProteoSAFe/result_json.jsp?task=d0e3af94f33f47acad56560de0c5a846&view=view_all_clusters_withID_beta"
        data = requests.get(url)
        clusters_object = json.loads(data.text)
        data = clusters_object["blockData"]
        assert(len(data) == 1373)

def test_gnps_molecule_explorer():
    for target in TARGET_WEB_SERVERS:
        url = "https://" + target + "/ProteoSAFe/result_json.jsp?task=698fc5a09db74c7492983b3673ff5bf6&view=view_aggregate_molecule_dataset"
        data = requests.get(url)
        clusters_object = json.loads(data.text)
        data = clusters_object["blockData"]
        assert(len(data) > 1000)
        url = "https://" + target + "/ProteoSAFe/result_json.jsp?task=698fc5a09db74c7492983b3673ff5bf6&view=view_aggregate_dataset_network"
        data = requests.get(url)
        datasets = json.loads(data.text)
        dataset_network = datasets["blockData"]
        assert(len(dataset_network) > 500)
