from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import unittest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

import HtmlTestRunner


# Test Script123
class LoginTest(unittest.TestCase):

        def setUp(self):
            print("Test Case Started")



        def test_loginTc1(self):
            driver = webdriver.Chrome(executable_path="C:\\PythonProjects\\Python_E2E\\drivers\\chromedriver.exe")
            driver.implicitly_wait(20)
            driver.maximize_window()
            driver.get("https://learn.letskodeit.com/p/practice")
            login=LoginPage(driver)
            login.Login()
            homepage = HomePage(driver)
            homepage.validate_homepage("abc@email.com","xxxx")
            driver.close()



        def test_loginTc2(self):
            driver = webdriver.Chrome(executable_path="C:\\PythonProjects\\Python_E2E\\drivers\\chromedriver.exe")
            driver.implicitly_wait(20)
            driver.maximize_window()
            driver.get("https://learn.letskodeit.com/p/practice")
            login = LoginPage(driver)
            login.Login()
            homepage = HomePage(driver)
            homepage.validate_homepage("thanu@email.com", "xxxx")
            driver.close()


        def tearDown(self):
            print("Test Completed")

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\PythonProjects\\Python_E2E\\reports"))


