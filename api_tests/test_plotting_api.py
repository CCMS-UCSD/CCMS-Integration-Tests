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

    # mzXML test, scan
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=fd246a746e0749c5ad0403be265bb2ea&block=0&file=FILE-%3Ef.MSV000079514%2Fccms_peak%2FRAW%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzXML&scan=524&index=-1&peptide=*..*&trim=true&format=JSON&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzXML test, bruker test
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&file=FILE-%3EMSV000078556%2Fccms_peak%2FHuman_Swabs%2FMan%2F3m__BA12_01_1117.mzXML&scan=4146&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true&format=JSON".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzML test, bruker test
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&file=FILE-%3EMSV000085120%2Fccms_peak%2FPlate%202%2FBAX100_5x_GB1_01_23264.mzML&scan=503&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true&format=JSON".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()
    
    # mzXML test, index
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000079514%2Fccms_peak%2FRAW%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzXML&index=11&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzML test, scan
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&file=FILE-%3Ef.MSV000079514%2Fccms_peak%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzML&scan=524&index=-1&peptide=*..*&trim=true&format=JSON&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzML test, index
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000079514%2Fccms_peak%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzML&index=11&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # Testing MGF
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.mgf&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true&format=JSON".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # Testing PKLBIN
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.pklbin&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true&format=JSON".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # Testing mzXML
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&file=FILE-%3Espec%2Fspec-00001.mzXML&scan=171&peptide=*..*&force=true&format=JSON".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # Testing MS1 scan
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&file=FILE-%3Ef.MSV000079514%2Fccms_peak%2FAdrenal%20gland%2FLTQ-Orbitrap%20Elite%2F49%2FAdult_Adrenalgland_Gel_Elite_49_f01.mzML&scan=521&index=-1&peptide=*..*&trim=true&format=JSON&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:115 (MS:1000771, "scan=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000081515%2Fraw%2Fblank1_pos_91_01_5418.mzML&nativeid=scan%3D115%2Cindex%3D115%2Cspectrum%3D115%2CscanId%3D115%2Cquery%3D115%2Cdatabasekey%3D115&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:272 (MS:1000772, "scan=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000081778%2Fccms_peak%2F20170619_HW_tilbutsf_net10UL.mzML&nativeid=scan%3D272%2Cindex%3D272%2Cspectrum%3D272%2CscanId%3D272%2Cquery%3D272%2Cdatabasekey%3D272&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:13126 (MS:1000776, "scan=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000082429%2Fpeak%2F11839_30288_Empty_MEF_BR1_071016.mzML&nativeid=scan%3D13126%2Cindex%3D13126%2Cspectrum%3D13126%2CscanId%3D13126%2Cquery%3D13126%2Cdatabasekey%3D13126&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:0 (MS:1000774, "index=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000079811%2Fpeak%2FMS2%2F20160112_P10_SEG_HIGH.mzML&nativeid=scan%3D0%2Cindex%3D0%2Cspectrum%3D0%2CscanId%3D0%2Cquery%3D0%2Cdatabasekey%3D0&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:1 (MS:1000777, "spectrum=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000082504%2Fccms_peak%2FN.%20synne._normal%20condition_10V_3%2F94_10V3.mzML&nativeid=scan%3D1%2Cindex%3D1%2Cspectrum%3D1%2CscanId%3D1%2Cquery%3D1%2Cdatabasekey%3D1&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:106274 (MS:1001508, "scanId=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000080010%2Fpeak%2FSMC_AGP_D1_H1_MS1.mzML&nativeid=scan%3D106274%2Cindex%3D106274%2Cspectrum%3D106274%2CscanId%3D106274%2Cquery%3D106274%2Cdatabasekey%3D106274&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:0,1,3757 (MS:1000768, "controllerType=? controllerNumber=? scan=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000082500%2Fpeak%2FOlesya-4T1_balbc_1.mzML&nativeid=controllerType%3D0%20controllerNumber%3D1%20scan%3D3757%2Cfunction%3D0%20process%3D1%20scan%3D3757%2Cdeclaration%3D0%20collection%3D1%20scan%3D3757%2Cframe%3D0%20scan%3D1%20frameType%3D3757&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:2,0,1 (MS:1000769, "function=? process=? scan=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000084954%2Fpeak%2F040220025.mzML&nativeid=controllerType%3D2%20controllerNumber%3D0%20scan%3D1%2Cfunction%3D2%20process%3D0%20scan%3D1%2Cdeclaration%3D2%20collection%3D0%20scan%3D1%2Cframe%3D2%20scan%3D0%20frameType%3D1&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()

    # mzML test, nativeId:1,1,7,2 (MS:1000770, "sample=? period=? cycle=? experiment=?")
    url = "https://{}/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&block=0&format=JSON&file=FILE-%3EMSV000084497%2Fpeak%2Fmzml%2FEllis_041_2781_261_01.mzML&nativeid=sample%3D1%20period%3D1%20cycle%3D7%20experiment%3D2&peptide=*..*&uploadfile=True&task=4f2ac74ea114401787a7e96e143bb4a1&force=true".format(server_url)
    print(url)
    r = requests.get(url, verify=False)
    r.raise_for_status()
    r.json()
