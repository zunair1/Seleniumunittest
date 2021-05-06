import time

from Pages.LoginPage import loginPage
from configData.testData import TestData
from TestCases.testRunner import TestRunner


class doLoginTest(TestRunner):

    def test_login(self):
        driver = self.driver
        loginPageObj = loginPage(driver)
        loginPageObj.clickSignInButtonOnHomePage()
        time.sleep(3)
        loginPageObj.setUsername(TestData.EMAIL)
        loginPageObj.setPassword(TestData.PASSWORD)
        time.sleep(3)
        loginPageObj.clickLoginButton()
