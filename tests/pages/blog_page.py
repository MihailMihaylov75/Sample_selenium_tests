__author__ = 'Mihail Mihaylov'

from tests.page_model.blog_page import BlogPageLocators
from tests.pages.base_page import BasePage


class BlogPage(BasePage):
    """
    Blog page class.
    """
    @property
    def url(self):
        """
        Get the url of the blog page of the app.
        :return: Url of the blog page.
        """
        return super(BlogPage, self).url + '/blog'

    @property
    def home(self):
        """
        Find the link to home page element.
        :return: Link to home page web element
        """
        return self.driver.find_element(*BlogPageLocators.HOME)

    @property
    def posts_section(self):
        """
        Find the link to post page element.
        :return: Link to post page web element
        """
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        """
        Find the link to posts elements.
        :return: Link to posts web element
        """
        return self.driver.find_element(*BlogPageLocators.POST)
