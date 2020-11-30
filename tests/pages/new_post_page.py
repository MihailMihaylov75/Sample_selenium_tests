__author__ = 'Mihail Mihaylov'

from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage
from tests.page_model.new_post_page import NewPostPageLocators
import selenium

print(selenium.__version__)


class NewPostPage(BasePage):
    @property
    def url(self):
        """
        Get the url of the post page of the app.
        :return: Url of the post page.
        """
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM)

    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
