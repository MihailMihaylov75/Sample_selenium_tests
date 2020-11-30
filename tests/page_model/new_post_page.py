__author__ = 'Mihail Mihaylov'
from selenium.webdriver.common.by import By


class NewPostPageLocators:
    """Class that contains locators for posts page"""
    NEW_POST_FORM = By.ID, 'post-form'
    TITLE_FIELD = By.ID, 'title'
    CONTENT_FIELD = By.ID, 'content'
    SUBMIT_BUTTON = By.ID, 'create-post'
