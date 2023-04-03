
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest, time, re

import warnings
warnings.filterwarnings('ignore')

class TestInterfaceready(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.vars = {}
        self.base_url = os.environ.get("SERVER_URL", "https://gnps.ucsd.edu")

    def tearDown(self):
        self.driver.quit()

    def test_interface_positive_gnps(self):
        self.driver.get("{}/ProteoSAFe/result.jsp?view=network_displayer&componentindex=9&task=5b4fa89c73344360b8b915a3af9ea7d4&test=true".format(self.base_url))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fa-check-circle")))
        nodes = self.driver.execute_script("return clusterinfo_data;")
        assert len(nodes) == 16
        edges = self.driver.execute_script("return pairs_data;")
        assert len(edges) == 29

    def test_interface_negative_gnps(self):
        self.driver.get("{}/ProteoSAFe/result.jsp?view=network_displayer&componentindex=54564&task=5b4fa89c73344360b8b915a3af9ea7d4&test=true".format(self.base_url))
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fa-check-circle")))
        nodes = self.driver.execute_script("return clusterinfo_data;")
        assert len(nodes) == 0
        edges = self.driver.execute_script("return pairs_data;")
        assert len(edges) == 0

if __name__ == "__main__":
    unittest.main()
