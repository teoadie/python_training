__author__ = 'Teo'
from page.new_group_page import GroupPage


class GroupUtils:

    def __init__(self, app):
        self.app = app
        self.group_page = GroupPage(app)

    def create(self, group):
        # Create group
        self.open_groups_page()
        self.fill_group_data(group)
        # Confirm group creation
        self.group_page.confirm_group_creation()
        # Return to home page
        self.return_to_groups_page()

    def open_groups_page(self):
        # Open groups page
        wd = self.app.wd
        wd.find_element_by_link_text('groups').click()

    def fill_group_data(self, group):
        # Init group creation
        wd = self.app.wd
        wd.find_element_by_name('new').click()
        # Fill group data
        if group != None:
            self.group_page.fill_group_page(group)
        else:
            # If group is null, just clear form
            self.group_page.clear_new_group_form()

    def return_to_groups_page(self):
        # Return to group page
        wd = self.app.wd
        wd.find_element_by_link_text('group page').click()

    def delete_first_group(self):
        self.open_groups_page()
        wd = self.app.wd
        # Select first group
        wd.find_element_by_name('selected[]').click()
        # Delete it
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()
