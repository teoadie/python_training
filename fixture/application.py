__author__ = 'Teo'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group_fixture import GroupUtils
from fixture.contact_fixture import ContactUtils
from page.main_page import MainPage


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.group = GroupUtils(self)
        self.contact = ContactUtils(self)
        self.session = MainPage(self)

    def destroy(self):
        self.wd.quit()
