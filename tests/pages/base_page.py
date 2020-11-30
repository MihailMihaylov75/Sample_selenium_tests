__author__ = 'Mihail Mihaylov'


from tests.page_model.base_page import BasePageLocators

URL = 'http://127.0.0.1:5000/'


class BasePage:
    """
    Base page class.
    """

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        """
        Get the url of the app.
        :return: Url of the app.
        """
        return URL

    def find_element(self, by, value):
        """
        Find an element given a By strategy and locator.
        :param by: Type of locator
        :param value: Locator value
        :return:  Web element - the element if it was found
        """
        return self.driver.find_element(by, value)

    @property
    def title(self):
        """
        Find a title element of the base page.
        :return: Title web element
        """
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        """
        Find a link to blog page of the base page.
        :return: Web element - link to blog page.
        """
        return self.find_element(*BasePageLocators.NAV_LINKS)
