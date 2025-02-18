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
        self.driver.implicitly_wait(15)
        self.base_url = os.environ.get("SERVER_URL", "https://gnps.ucsd.edu")
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    # Makes sure some tables show up properly on library pages
    def test_library_page_table(self):
        self.driver.get("{}/ProteoSAFe/libraries.jsp?test=true".format(self.base_url))
        
        time.sleep(15)
        
        elements = self.driver.find_element(by=By.ID, value="other_library_spectra.library_membership_input")

    def test_library_page_table2(self):
        self.driver.get("{}/ProteoSAFe/gnpslibrary.jsp?library=GNPS-LIBRARY&test=true".format(self.base_url))
        
        time.sleep(15)
        
        elements = self.driver.find_element(by=By.ID, value="main.spectrum_id_input")

        

if __name__ == "__main__":
    unittest.main()
