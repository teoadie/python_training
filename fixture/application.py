__author__ = 'Teo'
from selenium import webdriver
from fixture.group_fixture import GroupUtils
from fixture.contact_fixture import ContactUtils
from page.main_page import MainPage


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.group = GroupUtils(self)
        self.contact = ContactUtils(self)
        self.session = MainPage(self)
        self.base_url = base_url
        self.default_login = None
        self.default_password = None

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def set_default_user(self, default_login, default_password):
        self.default_login = default_login
        self.default_password = default_password
