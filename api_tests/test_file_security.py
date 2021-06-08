#!/usr/bin/python

import os
import requests

# TODO: replace these with references to GitHub secrets
TEST_CREDENTIALS = {}
TEST_CREDENTIALS["regular"] = {}
TEST_CREDENTIALS["regular"]["username"] = os.environ.get("TEST_USERNAME")
TEST_CREDENTIALS["regular"]["password"] = os.environ.get("TEST_PASSWORD")
TEST_CREDENTIALS["admin"] = {}
TEST_CREDENTIALS["admin"]["username"] = os.environ.get("ADMIN_USERNAME")
TEST_CREDENTIALS["admin"]["password"] = os.environ.get("ADMIN_PASSWORD")

# test parameters
TEST_HOST = "massive.ucsd.edu"
TEST_URLS = {}

# unauthenticated (i.e. guest) user
TEST_URLS["unauthenticated"] = {}
TEST_URLS["unauthenticated"]["authorized"] = [
    # direct file download via DownloadResultFile API:
    # general task result file - "t." file descriptor
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=t.4f2ac74ea114401787a7e96e143bb4a1/params/params.xml",
    # general task result file - "u." file descriptor
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=u.mwang87/4f2ac74ea114401787a7e96e143bb4a1/result/2c46386b5fd74a6983444c338620131a",
    # general task input file - symlinked to private user file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=t.71479437888f465189c39e3fdd47aee3/spec/spec-00000.mgf",
    # private user file
    # TODO: this should require authorization as soon as proper task cloning support is implemented
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.test/demo/Lens/93yo_sol_31_32.mgf",
    # public dataset file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000079852/ccms_parameters/params.xml",

    # plugin invocation via DownloadResultFile API:
    # private user file (in a general task context)
    # TODO: should this require authorization as soon as proper task cloning support is implemented?
    #       tasks routinely make requests like this (i.e using demangled user paths),
    #       so disallowing this would likely break standard result view behavior
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=fd4063b2271444de8d037f7378ef3498&block=0&format=JSON&file=FILE-%3Ef.test%2Fintegration_test_inputs%2Fmgf%2Fspecs_ms.mgf&scan=-1&index=452&peptide=*..*&trim=true",
    # public dataset file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=120ab12f58594dd29c5a71de529a9686&block=0&format=JSON&file=FILE-%3Ef.MSV000079852%2Fpeak%2Fpeak%2FColorectalCancer%2FTCGA-A6-3807-01A-22_Proteome_VU_20121019%2FmzML_data%2FTCGA-A6-3807-01A-22_W_VU_20121019_A0218_4I_R_FR01.mzML.gz&scan=443&index=-1&peptide=*..*&trim=true",

    # result view display:
    # TODO: this should really test the main result view page, but currently this page doesn't
    #       actually throw an HTTP error, it just prints out an error message for the end user
    #       to see; will need something like Selenium to properly test the actual result page
    # general task results - client-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=23e1c7ff0f804a35ba95ea0329da91d1&view=view_result_list",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=t.23e1c7ff0f804a35ba95ea0329da91d1/statistics/5d4a2a38122c4f9dbb22bf506c95a964.tsv",
    # general task results - server-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=23e1c7ff0f804a35ba95ea0329da91d1&view=group_by_spectrum&file=u.test%2F23e1c7ff0f804a35ba95ea0329da91d1%2Fresult%2Ftsv-00000.mzTab",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=t.23e1c7ff0f804a35ba95ea0329da91d1/result/tsv-00000.mzTab",
    # public dataset results - client-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=120ab12f58594dd29c5a71de529a9686&view=view_result_list",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000079852/ccms_statistics/statistics.tsv",
    # public dataset results - server-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=120ab12f58594dd29c5a71de529a9686&view=group_by_spectrum&file=f.MSV000079852%2Fccms_result%2Fresult%2FColorectalCancer%2FTCGA-A6-3807-01A-22_Proteome_VU_20121019.mzTab",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000079852/ccms_result/result/ColorectalCancer/TCGA-A6-3807-01A-22_Proteome_VU_20121019.mzTab",

    # USI resolution:
    # general task input file - symlinked to private user file
    # TODO: this should really test the main USI resolution page, but currently there are no file
    #       access controls in place for this page, only for the underlying specplot call
    #"https://" + TEST_HOST + "/ProteoSAFe/usi.jsp#%7B%22usi%22%3A%22mzspec%3AMassIVE%3ATASK-fd4063b2271444de8d037f7378ef3498-peak-00000%3Aindex%3A451%3AFIIPSPK%2F2%22%2C%22searched_button%22%3A%22spectra%22%7D",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=4f2ac74ea114401787a7e96e143bb4a1&block=0&format=JSON&file=FILE-%3Eu.ccms%2Ffd4063b2271444de8d037f7378ef3498%2Fpeak%2Fpeak-00000.mgf&index=452&peptide=*..*&charge=2&uploadfile=True",
    # public dataset file
    #"https://" + TEST_HOST + "/ProteoSAFe/usi.jsp#%7B%22usi%22%3A%22mzspec%3APXD000561%3AAdult_CD4Tcells_bRP_Elite_28_f15%3Ascan%3A12517%3ASYEAALLPLYMEGGFVEVIHDK%2F4%22%2C%22searched_button%22%3A%22spectra%22%7D"
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=4f2ac74ea114401787a7e96e143bb4a1&block=0&format=JSON&file=FILE-%3EMSV000079514%2Fccms_peak%2FCD4%20Tcells%2FLTQ-Orbitrap%20Elite%2F28%2FAdult_CD4Tcells_bRP_Elite_28_f15.mzML&scan=12517&peptide=*..*&charge=4&uploadfile=True"
]
TEST_URLS["unauthenticated"]["unauthorized"] = [
    # direct file download via DownloadResultFile API:
    # private dataset file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000078949/peak/HC2_1E2_MSA.mzid_HC2_1E2_MSA.MGF",

    # plugin invocation via DownloadResultFile API:
    # private dataset file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=a64b59e1be2043639470d39156a30025&block=0&format=JSON&file=FILE-%3Ef.MSV000078949%2Fpeak%2FHC2_1E2_MSA.mzid_HC2_1E2_MSA.MGF&scan=-1&index=63&peptide=*..*&trim=true",

    # result view display:
    # private dataset results - client-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=a64b59e1be2043639470d39156a30025&view=view_result_list",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000078949/ccms_statistics/statistics.tsv",
    # private dataset results - server-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=a64b59e1be2043639470d39156a30025&view=group_by_spectrum&file=f.MSV000078949%2Fccms_result%2FHC2_1E2_MSA.mzTab",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000078949/ccms_result/HC2_1E2_MSA.mzTab",

    # USI resolution:
    # private dataset file
    #"https://" + TEST_HOST + "/ProteoSAFe/usi.jsp#%7B%22usi%22%3A%22mzspec%3AMSV000078949%3AHC2_1E2_MSA.mzid_HC2_1E2_MSA.MGF%3Aindex%3A64%3ADESGPSIVHR%2F2%22%2C%22searched_button%22%3A%22spectra%22%7D"
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=4f2ac74ea114401787a7e96e143bb4a1&block=0&format=JSON&file=FILE-%3EMSV000078949%2Fpeak%2FHC2_1E2_MSA.mzid_HC2_1E2_MSA.MGF&index=65&peptide=*..*&charge=2&uploadfile=True"
]

# regular test user - not admin
TEST_URLS["authenticated_regular"] = {}
TEST_URLS["authenticated_regular"]["authorized"] = []
# regular users should have access to everything that guests can access
TEST_URLS["authenticated_regular"]["authorized"].extend(TEST_URLS["unauthenticated"]["authorized"])
# everything in the guest unauthorized list should accessible to this test user
TEST_URLS["authenticated_regular"]["authorized"].extend(TEST_URLS["unauthenticated"]["unauthorized"])
TEST_URLS["authenticated_regular"]["unauthorized"] = [
    # direct file download via DownloadResultFile API:
    # private dataset file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000081135/peak/spectrum_library_mgf_splits/0.mgf",

    # plugin invocation via DownloadResultFile API:
    # private dataset file
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=2c6f9394ec2a4253941abc87296194aa&block=0&format=JSON&file=FILE-%3Ef.MSV000081135%2Fpeak%2Fspectrum_library_mgf_splits%2F57.mgf&scan=1&index=-1&peptide=*..*&trim=true",

    # result view display:
    # private dataset results - client-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=2c6f9394ec2a4253941abc87296194aa&view=view_result_list",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000081135/ccms_statistics/statistics.tsv",
    # private dataset results - server-side
    #"https://" + TEST_HOST + "/ProteoSAFe/result.jsp?task=2c6f9394ec2a4253941abc87296194aa&view=group_by_spectrum&file=f.MSV000081135%2Fccms_result%2Fmassive-kb.mzTab",
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?file=f.MSV000081135/ccms_result/massive-kb.mzTab",

    # USI resolution:
    # private dataset file
    #"https://" + TEST_HOST + "/ProteoSAFe/usi.jsp#%7B%22usi%22%3A%22mzspec%3AMSV000081135%3A57.mgf%3Ascan%3A1%3A%5B%2B42.010565%5D-AAAAAAAAEQQSSNGPVKK%2F3%22%7D"
    "https://" + TEST_HOST + "/ProteoSAFe/DownloadResultFile?invoke=annotatedSpectrumImageText&task=4f2ac74ea114401787a7e96e143bb4a1&block=0&format=JSON&file=FILE-%3EMSV000081135%2Fpeak%2Fspectrum_library_mgf_splits%2F57.mgf&scan=1&peptide=*..*&charge=3&uploadfile=True"
]

# admin user
TEST_URLS["authenticated_admin"] = {}
TEST_URLS["authenticated_admin"]["authorized"] = []
# admin users should have access to everything that guests and regular users can access
TEST_URLS["authenticated_admin"]["authorized"].extend(TEST_URLS["authenticated_regular"]["authorized"])
# everything in the regular user unauthorized list should be accessible to admins
TEST_URLS["authenticated_admin"]["authorized"].extend(TEST_URLS["authenticated_regular"]["unauthorized"])

# test file accesses by a guest user
def test_unauthenticated_file_access():
    print("Testing ProteoSAFe file accesses by unauthorized (i.e. guest) user...")
    # test URLs that should be authorized without authentication
    print("  Should work:")
    for url in TEST_URLS["unauthenticated"]["authorized"]:
        print("    " + url)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    # test URLs that should not be authorized without authentication
    print("  Should fail:")
    for url in TEST_URLS["unauthenticated"]["unauthorized"]:
        print("    " + url)
        response = requests.get(url, timeout=10)
        try:
            assert response.status_code == 403
        except AssertionError:
            print("      Did not fail as expected (got status code " + str(response.status_code) + ")")
            raise

# test file accesses by a regular user
def test_authenticated_regular_user_file_access():
    print("Testing ProteoSAFe file accesses by authorized regular (i.e. non-admin) user...")
    # login as regular (i.e. non-admin) test user
    print("  Logging in as test user [" + TEST_CREDENTIALS["regular"]["username"] + "]...")
    session = get_proteosafe_session(TEST_CREDENTIALS["regular"]["username"], TEST_CREDENTIALS["regular"]["password"])
    # test URLs that should be authorized for this test user
    print("  Should work:")
    for url in TEST_URLS["authenticated_regular"]["authorized"]:
        print("    " + url)
        response = session.get(url, timeout=10)
        response.raise_for_status()
    # test URLs that should not be authorized for this test user
    print("  Should fail:")
    for url in TEST_URLS["authenticated_regular"]["unauthorized"]:
        print("    " + url)
        response = session.get(url, timeout=10)
        try:
            assert response.status_code == 403
        except AssertionError:
            print("      Did not fail as expected (got status code " + str(response.status_code) + ")")
            raise

# test file accesses by an admin user
def test_authenticated_admin_user_file_access():
    print("Testing ProteoSAFe file accesses by authorized admin user...")
    # login as admin test user
    print("  Logging in as test user [" + TEST_CREDENTIALS["admin"]["username"] + "]...")
    session = get_proteosafe_session(TEST_CREDENTIALS["admin"]["username"], TEST_CREDENTIALS["admin"]["password"])
    # test URLs that should be authorized for this admin user
    print("  Should work:")
    for url in TEST_URLS["authenticated_admin"]["authorized"]:
        print("    " + url)
        response = session.get(url, timeout=10)
        response.raise_for_status()

# helper function get an authenticated ProteoSAFe session
def get_proteosafe_session(username, password):
    url = "https://" + TEST_HOST + "/ProteoSAFe/user/login.jsp"
    parameters = {
        "user": username,
        "password": password,
        "login": "Sign in"
    }
    session = requests.Session()
    response = session.post(url, parameters)
    if response.status_code != 200:
        raise Exception("Got status code [" + str(response.status_code) + "] from login attempt for user [" + username + "].")
    else:
        return session

def main():
    test_unauthenticated_file_access()
    print("")
    test_authenticated_regular_user_file_access()
    print("")
    test_authenticated_admin_user_file_access()

if __name__ == "__main__":
    main()
