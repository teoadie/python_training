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

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
