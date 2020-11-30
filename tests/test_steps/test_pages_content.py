__author__ = 'Mihail Mihaylov'

import unittest

from tests.pages.base_page import BasePage, URL
from tests.pages.blog_page import BlogPage
from tests.pages.browser_set_up import Browser


class TestHomePageContent(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().get_browser("chrome")
        self.driver.get(URL)
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
        self.driver = Browser().get_browser("chrome")
        self.driver.get(URL + '/blog')
        self.page = BlogPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_blog_page_has_link_to_home(self):
        tag = self.page.home
        assert tag is not None
        assert tag.is_displayed()
