__author__ = 'Mihail Mihaylov'

from tests.page_model.blog_page import BlogPageLocators
from tests.pages.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def home(self):
        return self.driver.find_element(*BlogPageLocators.HOME)

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_element(*BlogPageLocators.POST)
