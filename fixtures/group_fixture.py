__author__ = 'Teo'
from selenium.webdriver.firefox.webdriver import WebDriver
from pages import new_group_page
from pages import main_page


class GroupFixture:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def destroy(self):
        self.wd.quit()

    def open_group_page_and_create_new_group(self, group):
        wd = self.wd
        # Create group
        self.open_groups_page()
        self.create_group(group)
        self.return_to_groups_page()

    def open_groups_page(self):
        # Open groups page
        wd = self.wd
        wd.find_element_by_link_text('groups').click()

    def create_group(self, group):
        # Init group creation
        wd = self.wd
        wd.find_element_by_name('new').click()
        # Fill group data
        if group != None:
            new_group_page.fill_group_page(wd, group)
        else:
            # If group is null, just clear form
            new_group_page.clear_new_group_form(wd)
        # Confirm group creation
        new_group_page.confirm_group_creation(wd)

    def return_to_groups_page(self):
        # Return to group page
        wd = self.wd
        wd.find_element_by_link_text('group page').click()

    def logout(self):
        # Return to login page
        main_page.logout(self.wd)

    def login(self):
        wd = self.wd
        # Open home page
        main_page.open_home_page(wd)
        # Login by admin
        main_page.login_as_admin(wd)