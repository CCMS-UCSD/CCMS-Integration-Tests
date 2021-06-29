# Generated by Selenium IDE
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest, time, re

import warnings
warnings.filterwarnings('ignore')

class TestInterfaceready(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
        self.driver.implicitly_wait(1)
        self.vars = {}
        self.base_url = os.environ.get("SERVER_URL", "https://gnps.ucsd.edu")

    def tearDown(self):
        self.driver.quit()

    def test_gnps_fbmn(self):
        url = "{}/ProteoSAFe/result.jsp?task=269d0b4eaa8d465ca6d95527af04feae&view=network_pairs_specnets_allcomponents&test=true".format(self.base_url)
        print(url)
        self.driver.get(url)
        
        time.sleep(30)

        for entry in self.driver.get_log('browser'):
            print(entry)
        
        # Checking that this does exist
        elements = self.driver.find_element_by_id("main.CLUSTERID1_lowerinput")

    def test_gnps_networking(self):
        url = "{}/ProteoSAFe/result.jsp?task=92b9d140de144bb1afc0f0775858d453&view=view_raw_spectra&test=true".format(self.base_url)
        print(url)
        self.driver.get(url)
        
        time.sleep(30)
        
        # Checking that this does exist
        elements = self.driver.find_element_by_id("main.AllFiles_input")

    


if __name__ == "__main__":
    unittest.main()