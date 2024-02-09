# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest, time, re
import os

import warnings
warnings.filterwarnings('ignore')

class TestTaskList(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.base_url = os.environ.get("SERVER_URL", "https://gnps.ucsd.edu/")
        print("Testing", self.base_url)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_task_list(self):
        driver = self.driver
        # log in as test user
        print("Logging in as test user.")
        print("URL = {}/ProteoSAFe/user/login.jsp?test=true".format(self.base_url))
        driver.get("{}/ProteoSAFe/user/login.jsp?test=true".format(self.base_url))
        username_field = None
        for i in range(60):
            try:
                username_field = driver.find_element(by=By.NAME, value="user")
                if self.is_element_present(By.NAME, "user"): break
            except NoSuchElementException:
                pass
            time.sleep(1)
        else: self.fail("time out")
        username_field.clear()
        username_field.send_keys("test")
        password_field = driver.find_element(by=By.NAME, value="password")
        password_field.clear()
        password_field.send_keys(os.environ.get("CCMS_TESTUSER_PASSWORD"))
        driver.find_element(by=By.NAME, value="login").click()
        for i in range(60):
            try:
                if "Successful login" == driver.find_element(by=By.XPATH, value="//h1").text: break
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
        pagination_header = driver.find_element(by=By.XPATH, value="//div[@id=\"main_title\"]/following-sibling::div/span").text
        try: self.assertTrue(re.search(pattern, pagination_header) is not None)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
