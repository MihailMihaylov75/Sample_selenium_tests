__author__ = 'Mihail Mihaylov'

from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.ID, 'title'
    NAV_LINKS = By.ID, 'blog-link'
