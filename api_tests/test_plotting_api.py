import requests
from nose2.tools import params
import json

def test_internal_plot_api():
    url = "https://ccms-internal.ucsd.edu/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=8c2674bb0d40482fb813c83580fb0766&block=0&file=FILE-%3Ef.test%2Fdemo%2FLens%2Fspectra%2F93yo_sol_31_32.mgf&scan=-1&index=267&peptide=*..*&trim=true&force=true"
    r = requests.get(url, verify=False)
    r.raise_for_status()


def test_internal_plot_json():
    # JSON for USI
    url = "https://ccms-internal.ucsd.edu/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000081515%2Fccms_peak%2Fblank1_pos_91_01_5418.mzML&nativeid=scan%3D115%2Cindex%3D115%2Cspectrum%3D115%2CscanId%3D115%2Cquery%3D115%2Cdatabasekey%3D115&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1"
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()



@params("gnps.ucsd.edu", "proteomics2.ucsd.edu",  "proteomics3.ucsd.edu")
def test_internal_old_api(server_url):
    # Testing MGF
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.mgf&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true".format(server_url)
    r = requests.get(url)
    r.raise_for_status()

    # Testing PKLBIN
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.pklbin&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true".format(server_url)
    r = requests.get(url)
    r.raise_for_status()

    # Testing mzXML
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&file=FILE-%3Espec%2Fspec-00001.mzXML&scan=171&peptide=*..*&force=true".format(server_url)
    r = requests.get(url)
    r.raise_for_status()


def test_json_api():
    server_url = "proteomics3.ucsd.edu"

    # mzXML test
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=fd246a746e0749c5ad0403be265bb2ea&block=0&file=FILE-%3Ef.MSV000079514%2Fccms_peak%2FRAW%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzXML&scan=524&index=-1&peptide=*..*&trim=true&format=JSON&force=true".format(server_url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&file=FILE-%3Ef.MSV000079514%2Fccms_peak%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzML&scan=524&index=-1&peptide=*..*&trim=true&format=JSON&force=true".format(server_url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # Testing MGF
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.mgf&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true".format(server_url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # Testing PKLBIN
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.pklbin&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true".format(server_url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # Testing mzXML
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&file=FILE-%3Espec%2Fspec-00001.mzXML&scan=171&peptide=*..*&force=true".format(server_url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()