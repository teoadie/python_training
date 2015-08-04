# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class add_group_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_groups_page(wd)
        self.create_group(wd, group_name='Best friends', header='My best friends', footer='Hell yeah')
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_groups_page(wd)
        self.create_group(wd, group_name='', header='', footer='')
        self.return_to_groups_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        # open home page
        wd.get('http://localhost/addressbook/')

    def login(self, wd, username, password):
        # Fill login field
        wd.find_element_by_name('user').click()
        wd.find_element_by_name('user').clear()
        wd.find_element_by_name('user').send_keys(username)
        # Fill password field
        wd.find_element_by_name('pass').click()
        wd.find_element_by_name('pass').clear()
        wd.find_element_by_name('pass').send_keys(password)
        # Confirm login
        wd.find_element_by_css_selector('input[type=\'submit\']').click()

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text('Logout').click()

    def open_groups_page(self, wd):
        # Open groups page
        wd.find_element_by_link_text('groups').click()

    def create_group(self, wd, group_name, header, footer):
        # Init group creation
        wd.find_element_by_name('new').click()
        # Fill group data
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_keys(group_name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_keys(header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_keys(footer)
        # Confirm group creation
        wd.find_element_by_name('submit').click()

    def return_to_groups_page(self, wd):
        # Return to group page
        wd.find_element_by_link_text('group page').click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
