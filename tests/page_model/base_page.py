__author__ = 'Mihail Mihaylov'

from selenium.webdriver.common.by import By


class BasePageLocators:
    """Class that contains locators for base/home page"""
    TITLE = By.ID, 'title'
    NAV_LINKS = By.ID, 'blog-link'
