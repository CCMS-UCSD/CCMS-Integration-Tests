# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import os

import warnings
warnings.filterwarnings('ignore')

class TestTaskList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
        self.driver.implicitly_wait(30)
        self.base_url = os.environ.get("SERVER_URL", "https://proteomics3.ucsd.edu")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_task_list(self):
        driver = self.driver
        # log in as test user
        print("Logging in as test user.")
        driver.get("{}/ProteoSAFe/user/login.jsp?test=true".format(self.base_url))
        for i in range(60):
            try:
                if self.is_element_present(By.NAME, "user"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("test")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(os.environ.get("CCMS_TESTUSER_PASSWORD"))
        driver.find_element_by_name("login").click()
        for i in range(60):
            try:
                if "Successful login" == driver.find_element_by_xpath("//h1").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        # load task list page
        print("Loading task list page.")
        driver.get("{}/ProteoSAFe/jobs.jsp".format(self.base_url))
        time.sleep(5)

        # verify that task list navigator is present, and contains the expected text
        print("Verifying task list pagination header.")
        pattern = "^Hits [0-9]+ ~ 30 out of [0-9]+(,[0-9]{3})*$"
        pagination_header = driver.find_element_by_xpath("//div[@id=\"main_title\"]/following-sibling::div/span").text
        try: self.assertTrue(re.search(pattern, pagination_header) is not None)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
