__author__ = 'Mihail Mihaylov'

from selenium import webdriver
import unittest

from tests.pages.base_page import BasePage, URL
from tests.pages.blog_page import BlogPage


class TestHomePageContent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.page = BasePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_title_tag_shown(self):
        tag = self.page.title
        assert tag is not None
        assert tag.is_displayed()

    def test_title_tag_has_content(self):
        assert self.page.title.text == 'This is the homepage'

    def test_link_to_blog_page_shown(self):
        tag = self.page.navigation
        assert tag is not None
        assert tag.is_displayed()

    def test_link_to_blog_tag_has_content(self):
        assert self.page.navigation.text == 'Go to blog'


class TestBlogPageContent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.get(URL + '/blog')
        self.page = BlogPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_blog_page_has_link_to_home(self):
        tag = self.page.home
        assert tag is not None
        assert tag.is_displayed()
