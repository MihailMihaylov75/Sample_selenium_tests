__author__ = 'Mihail Mihaylov'
# Needed set up so that an instance can be made
# Download chromedriver:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# Download geckodriver for firefox
# https://github.com/mozilla/geckodriver/releases
# Download edge web driver for edge
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Download IE web driver for Internet Explorer
# https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver
# @TODO add for other browsers

from selenium import webdriver


class Browser(object):
    """Creates a new instance of given driver."""
    def __init__(self):
        self.driver = None

    def get_browser(self, browser_name):
        """
        Starts the service and then creates new instance of given driver.
        :param browser_name: Browser name one of the following: firefox, chrome, edge, ie
        :return: New instance of chosen driver
        """
        if browser_name == "firefox":
            self.driver = webdriver.Firefox()
        elif browser_name == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_name == "edge":
            self.driver = webdriver.Edge()
        elif browser_name == "ie":
            self.driver = webdriver.Ie()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver
