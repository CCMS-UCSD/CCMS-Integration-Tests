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
import unittest, time, re
import os

class TestInterfaceready(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(1)
        self.base_url = os.environ.get("SERVER_URL", "https://gnps.ucsd.edu")
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    # Makes sure some tables show up properly on library pages
    def test_library_page_table(self):
        self.driver.get("{}/ProteoSAFe/libraries.jsp?test=true".format(self.base_url))
        
        time.sleep(15)
        
        elements = self.driver.find_element_by_id("other_library_spectra.library_membership_input")

    def test_library_page_table2(self):
        self.driver.get("{}/ProteoSAFe/gnpslibrary.jsp?library=GNPS-LIBRARY&test=true".format(self.base_url))
        
        time.sleep(15)
        
        elements = self.driver.find_element_by_id("main.spectrum_id_input")

        

if __name__ == "__main__":
    unittest.main()