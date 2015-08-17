__author__ = 'Teo'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group_fixture import GroupUtils
from fixture.contact_fixture import ContactUtils
from page.main_page import MainPage


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.set_default_wait_element_time()
        self.group = GroupUtils(self)
        self.contact = ContactUtils(self)
        self.session = MainPage(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def set_minimum_wait_element_time(self):
        self.wd.implicitly_wait(0)

    def set_default_wait_element_time(self):
        self.wd.implicitly_wait(3)
