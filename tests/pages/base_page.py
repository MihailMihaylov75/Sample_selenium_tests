__author__ = 'Mihail Mihaylov'


from tests.page_model.base_page import BasePageLocators

URL = 'http://127.0.0.1:5000/'


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return URL

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    @property
    def title(self):
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.find_element(*BasePageLocators.NAV_LINKS)