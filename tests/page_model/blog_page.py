__author__ = 'Mihail Mihaylov'
from selenium.webdriver.common.by import By


class BlogPageLocators:
    POSTS_SECTION = By.ID, 'posts'
    POST = By.ID, 'add-post-link'
    HOME = By.ID, 'home-link'

