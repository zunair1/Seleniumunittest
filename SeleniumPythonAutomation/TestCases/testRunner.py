import unittest
from selenium import webdriver
import os
import sys
from configData.testData import TestData
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class TestRunner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Aksam Ali/PycharmProjects/SeleniumPyTest"
                                                      "/chromedriver_win32/chromedriver.exe")
        cls.driver.get(TestData.BASE_URL)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
