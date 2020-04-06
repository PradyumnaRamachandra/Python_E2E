import time

class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.username="//input[@id='user_email']"
        self.password="//input[@id='user_password']"

    def validate_homepage(self,Username,Password):
        self.driver.find_element_by_xpath(self.username).send_keys(Username)
        self.driver.find_element_by_xpath(self.password).send_keys(Password)
        time.sleep(2)


