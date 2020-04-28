import requests

def test_internal_plot_api():
    url = "https://ccms-internal.ucsd.edu/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=8c2674bb0d40482fb813c83580fb0766&block=0&file=FILE-%3Ef.test%2Fdemo%2FLens%2Fspectra%2F93yo_sol_31_32.mgf&scan=-1&index=267&peptide=*..*&trim=true"
    r = requests.get(url, verify=False)
    r.raise_for_status()

def test_internal_gnps_api():
    # Testing MGF
    url = "https://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&file=FILE-%3Espectra%2Fspecs_ms.mgf&scan=17&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&peptide=*..*&force=true"
    r = requests.get(url)
    r.raise_for_status()

    # Testing mzXML
    url = "https://gnps.ucsd.edu/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=1ad7bc366aef45ce81d2dfcca0a9a5e7&block=0&file=FILE-%3Espec%2Fspec-00001.mzXML&scan=171&peptide=*..*&force=true"
    r = requests.get(url)
    r.raise_for_status()