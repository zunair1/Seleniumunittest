from selenium.webdriver import ActionChains

from locators.Locators import locators


class SearchItemFromHomePage(locators):
    """constructor"""

    def __init__(self, driver):
        self.driver = driver

        self.SearchBoxOnHomePageId = locators.Search_box_On_Home_Page_By_id
        self.SearchSubmitButton = locators.Search_Submit_Button_By_name
        self.PrintedShiffonDressImage = locators.Image_Chiffon_Dress_By_xpath
        self.MoreButtonOnProduct = locators.More_Button_In_Image_By_xpath

    def SearchBoxOnHomePage(self, searchText):
        self.driver.find_element_by_id(self.SearchBoxOnHomePageId).send_keys(searchText)

    def clickSearchButton(self):
        self.driver.find_element_by_name(self.SearchSubmitButton).click()

    def ClickSearchedProduct(self):
        actions = ActionChains(self.driver)
        ImageLink = self.driver.find_element_by_xpath(self.PrintedShiffonDressImage)
        element = self.driver.find_element_by_xpath(self.MoreButtonOnProduct)

        actions.move_to_element(ImageLink)
        actions.click(element)
        actions.perform()
