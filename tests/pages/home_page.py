__author__ = 'Mihail Mihaylov'

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'
