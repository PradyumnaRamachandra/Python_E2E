from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
import HtmlTestRunner



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\PythonProjects\\Python_E2E\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        # cls.driver.get("https://learn.letskodeit.com/p/practice")

    def test_loginTc1(self):
        driver=self.driver
        driver.get("https://learn.letskodeit.com/p/practice")
        login=LoginPage(driver)
        # wait = WebDriverWait(driver, 20, poll_frequency=1)
        # element = wait.until(ec.element_to_be_clickable(("id", "txtUsername")))
        login.Login()

        homepage = HomePage(driver)
        # wait = WebDriverWait(driver, 20, poll_frequency=1)
        # element = wait.until(ec.element_to_be_clickable(("xpath", "//a[contains(text(),'Admin')]")))
        homepage.validate_homepage("abc@email.com","xxxx")
        # element = wait.until(ec.element_to_be_clickable(("id", "btnLogin")))

    def test_loginTc2(self):
        driver=self.driver
        driver.get("https://learn.letskodeit.com/p/practice")
        login=LoginPage(driver)
        # wait = WebDriverWait(driver, 20, poll_frequency=1)
        # element = wait.until(ec.element_to_be_clickable(("id", "txtUsername")))
        login.Login()

        homepage = HomePage(driver)
        # wait = WebDriverWait(driver, 20, poll_frequency=1)
        # element = wait.until(ec.element_to_be_clickable(("xpath", "//a[contains(text(),'Admin')]")))
        homepage.validate_homepage("abc@email.com","xxxx")
        # element = wait.until(ec.element_to_be_clickable(("id", "btnLogin")))


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")



if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/PythonProjects/Python_E2E/reports"))



