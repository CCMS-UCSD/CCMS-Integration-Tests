# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import os

class OverrideClonedTaskWorkflowVersion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = os.environ.get("SERVER_URL", "https://gnps.ucsd.edu")
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_override_cloned_task_workflow_version(self):
        driver = self.driver
        driver.get("{}/ProteoSAFe/user/login.jsp?test=true".format(self.base_url))
        # log in as test user
        print("Logging in as test user.")
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
                if "Successful login" == driver.find_element_by_xpath("//h1").text:
                    print("Successful login")
                    break
            except:
                raise
                pass
            time.sleep(1)
        else: self.fail("time out")

        # clone reference task (version "release_14") and verify that input form is loaded
        print("Cloning reference task with version release_14")
        driver.get(self.base_url + "/ProteoSAFe/index.jsp?task=0d5863e169464a069005c111ada37c30&test=true")
        
        time.sleep(5)

        driver.find_element_by_name("searchinterface")
        print(driver.page_source.encode("utf-8"))


        # Assuming there is only one small tag in the page, this could be violated later
        small_tags = driver.find_element_by_tag_name("small")
        version_text = small_tags.text
        version = version_text.replace("Version ", "")
        self.assertEqual(version, "release_14")


        # Cloning to version release_17
        print("Cloning reference task with version release_17")
        driver.get(self.base_url + "/ProteoSAFe/index.jsp?task=0d5863e169464a069005c111ada37c30&params={%22workflow_version%22:%22release_17%22}&test=true")

        time.sleep(5)

        # Assuming there is only one small tag in the page, this could be violated later
        small_tags = driver.find_element_by_tag_name("small")
        version_text = small_tags.text
        version = version_text.replace("Version ", "")
        self.assertEqual(version, "release_17")

        # Cloning to current, should be release_18 or greater
        print("Cloning reference task with version release_18")
        driver.get(self.base_url + "/ProteoSAFe/index.jsp?task=e95433bf446741dfb10fbe94153bfaee&params={%22workflow_version%22:%22current%22}&test=true")

        time.sleep(2)

        # Assuming there is only one small tag in the page, this could be violated later
        small_tags = driver.find_element_by_tag_name("small")
        version_text = small_tags.text
        version = version_text.replace("Version ", "")
        self.assertNotEqual(version, "release_14")
        self.assertNotEqual(version, "release_17")

    
    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException: 
            return False
        return True
    
    def is_alert_present(self):
        try: 
            self.driver.switch_to_alert()
        except NoAlertPresentException: 
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
