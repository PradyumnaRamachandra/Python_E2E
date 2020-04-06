class LoginPage():

    def __init__(self,driver):
        self.driver=driver

        # self.username_textfield="//input[@id='txtUsername']"
        # self.password_textfield="//input[@id='txtPassword']"
        self.login_button="//a[contains(text(),'Login')]"

    def Login(self):
        # self.driver.find_element_by_xpath(self.username_textfield).send_keys(Username)
        # self.driver.find_element_by_xpath(self.password_textfield).send_keys(Password)
        self.driver.find_element_by_xpath(self.login_button).click()

