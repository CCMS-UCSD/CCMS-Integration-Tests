
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest, time, re


class TestInterfaceready(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def test_interface_positive_gnps(self):
        self.driver.get("https://gnps.ucsd.edu/ProteoSAFe/result.jsp?view=network_displayer&componentindex=9&task=5b4fa89c73344360b8b915a3af9ea7d4&test=true")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fa-check-circle")))
        nodes = self.driver.execute_script("return clusterinfo_data;")
        assert len(nodes) == 16
        edges = self.driver.execute_script("return pairs_data;")
        assert len(edges) == 29

    def test_interface_negative_gnps(self):
        self.driver.get("https://gnps.ucsd.edu/ProteoSAFe/result.jsp?view=network_displayer&componentindex=54564&task=5b4fa89c73344360b8b915a3af9ea7d4&test=true")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fa-check-circle")))
        nodes = self.driver.execute_script("return clusterinfo_data;")
        assert len(nodes) == 0
        edges = self.driver.execute_script("return pairs_data;")
        assert len(edges) == 0

    def test_interface_positive_proteomics2(self):
        self.driver.get("https://proteomics3.ucsd.edu/ProteoSAFe/result.jsp?view=network_displayer&componentindex=9&task=5b4fa89c73344360b8b915a3af9ea7d4&test=true")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fa-check-circle")))
        nodes = self.driver.execute_script("return clusterinfo_data;")
        assert len(nodes) == 16
        edges = self.driver.execute_script("return pairs_data;")
        assert len(edges) == 29

    def test_interface_negative_proteomics2(self):
        self.driver.get("https://proteomics3.ucsd.edu/ProteoSAFe/result.jsp?view=network_displayer&componentindex=54564&task=5b4fa89c73344360b8b915a3af9ea7d4&test=true")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".fa-check-circle")))
        nodes = self.driver.execute_script("return clusterinfo_data;")
        assert len(nodes) == 0
        edges = self.driver.execute_script("return pairs_data;")
        assert len(edges) == 0

if __name__ == "__main__":
    unittest.main()