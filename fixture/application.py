__author__ = 'Teo'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group_fixture import GroupUtils
from fixture.contact_fixture import ContactUtils
from page.main_page import MainPage


class Application:

    def __init__(self):
        self.wd = WebDriver()
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
