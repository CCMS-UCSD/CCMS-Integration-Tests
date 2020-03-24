import requests


def test_massive_apis():
    url = "https://massive.ucsd.edu/ProteoSAFe//proxi/v0.1/datasets?filter=MSV000084741&function=datasets"

    r = requests.get(url)
    r.raise_for_status()


def test_massive_webpage():
    requests.get("http://massive.ucsd.edu/ProteoSAFe/datasets.jsp", timeout=10).raise_for_status() #Datasets Page
    requests.get("http://massive.ucsd.edu/ProteoSAFe/dataset.jsp?task=fd246a746e0749c5ad0403be265bb2ea", timeout=10).raise_for_status() #Dataset Page
    requests.get("http://massive.ucsd.edu/ProteoSAFe/MassiveServlet?function=reanalysis&task=fd246a746e0749c5ad0403be265bb2ea", timeout=10).raise_for_status() #Reanalysese
    requests.get("http://massive.ucsd.edu/ProteoSAFe/MassiveServlet?function=massivehistory&massiveid=MSV000079514", timeout=10).raise_for_status()
    requests.get("http://massive.ucsd.edu/ProteoSAFe/MassiveServlet?function=massivesummary&massiveid=MSV000079514", timeout=10).raise_for_status()


def test_massive_ftp():
    import urllib.request


    url = "ftp://massive.ucsd.edu/MSV000080469"
    print(url)
    urllib.request.urlopen(url)

    url = "ftp://massive.ucsd.edu/MSV000079146"
    print(url)
    urllib.request.urlopen(url)

    url = "ftp://massive.ucsd.edu/MSV000079339"
    print(url)
    urllib.request.urlopen(url)

    url = "ftp://massive.ucsd.edu/MSV000079341"
    print(url)
    urllib.request.urlopen(url)

    url = "ftp://massive.ucsd.edu/MSV000079344"
    print(url)
    urllib.request.urlopen(url)

    url = "ftp://massive.ucsd.edu/MSV000080469/peak/AMG_mzXML/10317.000006947.mzXML"
    print(url)
    urllib.request.urlopen(url)
    
def msstats_annotation_servlet():
    url = "https://ccms-internal.ucsd.edu/ProteoSAFe/MSStatsAnnotationServlet?filepath=f.benpullman%2FMSV000080025_mplex_calu3_MERS_CoV_response.csv%3B&header=Condition"
    r = requests.get(url)
    r.raise_for_status()
    
    url ="https://ccms-internal.ucsd.edu/ProteoSAFe/MSStatsAnnotationServlet?filepath=f.benpullman%2FMSV000080025_mplex_calu3_MERS_CoV_response.csv%3B&header=Missing"
    r = requests.get(url)
    assert(r.status_code == 400)
