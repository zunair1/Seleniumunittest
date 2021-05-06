import time

from Pages.SearchItemPage import SearchItemFromHomePage
from configData.testData import TestData
from TestCases.testRunner import TestRunner


class doSearchItemTest(TestRunner):

    def test_Search_Item(self):
        driver = self.driver
        SearchItemFromHomePageObj = SearchItemFromHomePage(driver)
        time.sleep(5)
        SearchItemFromHomePageObj.SearchBoxOnHomePage(TestData.ITEM)
        time.sleep(5)
        SearchItemFromHomePageObj.clickSearchButton()
        time.sleep(5)
        SearchItemFromHomePageObj.ClickSearchedProduct()
