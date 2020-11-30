__author__ = 'Mihail Mihaylov'

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        """
        Get the url of the app.
        :return: Url of the app.
        """
        return super(HomePage, self).url + '/'
