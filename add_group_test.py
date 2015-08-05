# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver
from model.group_data import Group
from pages import main_page
from pages import new_group_page


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
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        self.open_groups_page(wd)
        group = Group(name='Best friends', header='My best friends', footer='Hell yeah')
        self.create_group(wd, group)
        self.return_to_groups_page(wd)
        main_page.logout(wd)

    def test_add_group_with_spaces(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        self.open_groups_page(wd)
        group = Group(name='', header='', footer='')
        self.create_group(wd, group)
        self.return_to_groups_page(wd)
        main_page.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        self.open_groups_page(wd)
        # Init group creation
        wd.find_element_by_name('new').click()
        # Clear group form
        new_group_page.clear_new_group_form(wd)
        # Confirm group creation
        new_group_page.confirm_group_creation(wd)
        self.return_to_groups_page(wd)
        main_page.logout(wd)

    def open_groups_page(self, wd):
        # Open groups page
        wd.find_element_by_link_text('groups').click()

    def create_group(self, wd, group):
        # Init group creation
        wd.find_element_by_name('new').click()
        # Clear group form
        new_group_page.clear_new_group_form(wd)
        # Fill group data
        new_group_page.fill_group_page(wd, group)
        # Confirm group creation
        new_group_page.confirm_group_creation(wd)

    def return_to_groups_page(self, wd):
        # Return to group page
        wd.find_element_by_link_text('group page').click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
