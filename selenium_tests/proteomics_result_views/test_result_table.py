# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
import os

import warnings
warnings.filterwarnings('ignore')

class TestInterfaceready(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(1)
        self.base_url = os.environ.get("SERVER_URL", "https://proteomics3.ucsd.edu")
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    # This makes sure on client side tables, the autohiding works
    def test_client_table_autohide(self):
        url = "{}/ProteoSAFe/result.jsp?task=120ab12f58594dd29c5a71de529a9686&view=view_result_list&test=true".format(self.base_url)
        print(url)
        self.driver.get(url)
        
        time.sleep(5)

        # Positive control, making sure this does exist
        elements = self.driver.find_element(by=By.ID, value="main.Found_PSMs_lowerinput")
        
        # Checking that this doesn't exist
        with self.assertRaises(NoSuchElementException):
            elements = self.driver.find_element(by=By.ID, value="main.Invalid_PSM_rows_lowerinput")


    # This makes sure on server side tables, the autohiding works
    def test_server_table_autohide(self):
        url = "{}/ProteoSAFe/result.jsp?task=120ab12f58594dd29c5a71de529a9686&view=group_by_spectrum&file=f.MSV000079852%2Fccms_result%2Fresult%2FColorectalCancer%2FTCGA-A6-3807-01A-22_Proteome_VU_20121019.mzTab&test=true".format(self.base_url)
        print(url)
        self.driver.get(url)
        
        time.sleep(5)
        
        # Checking that this doesnt exist
        with self.assertRaises(NoSuchElementException):
            elements = self.driver.find_element(by=By.ID, value="main_search_engine_input")

    # This makes sure we don't autohide when sorting
    def test_server_sort_autohide(self):
        url = "{}/ProteoSAFe/result.jsp?task=4236c43b0d3a476a8e7f72aa00707e4b&view=view_differential&test=true#%7B%22table_sort_history%22%3A%22_dyn_%23adj.pvalue_asc%22%7D".format(self.base_url)
        print(url)
        self.driver.get(url)
        
        time.sleep(5)
        
        # print test environment browser console messages, if any
        console = self.driver.get_log("browser")
        if console:
            print("browser console:")
            print("----------")
            print(console)
            print("----------")
        
        # Checking that this does exist
        elements = self.driver.find_element(by=By.ID, value="view_differential__dyn_#adj.pvalue_asc")

if __name__ == "__main__":
    unittest.main()
