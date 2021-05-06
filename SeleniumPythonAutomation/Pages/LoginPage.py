from locators.Locators import locators


# pkg.file import class


class loginPage(locators):
    """constructor"""

    def __init__(self, driver):
        self.driver = driver

        self.SignInButtonOnHomePage = locators.SignIn_Button_On_Home_Page_By_xpath
        self.Login_Email = locators.Login_Email_By_id
        self.Login_Password = locators.Login_Password_By_id
        self.Login_Button = locators.Login_Button_By_id
        # self.Login_Email = "txtUsername"

    def clickSignInButtonOnHomePage(self):
        self.driver.find_element_by_xpath(self.SignInButtonOnHomePage).click()

    def setUsername(self, username):
        self.driver.find_element_by_id(self.Login_Email).send_keys(username)
    # self.driver.find_element_by_id("txtUsername").send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.Login_Password).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element_by_id(self.Login_Button).click()
