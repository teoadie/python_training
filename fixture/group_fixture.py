__author__ = 'Teo'
from page.new_group_page import GroupEditPage
from page.groups_page import GroupsPage


class GroupUtils:

    def __init__(self, app):
        self.app = app
        self.group_edit_page = GroupEditPage(app)
        self.groups_page = GroupsPage(app)

    def create(self, group):
        # Create group
        self.groups_page.click_new_group_button()
        self.group_edit_page.fill_group_page(group)
        # Confirm group creation
        self.group_edit_page.confirm_group_creation()
        # Return to home page
        self.return_to_groups_page()

    def open_groups_page(self):
        # Open groups page
        wd = self.app.wd
        wd.find_element_by_link_text('groups').click()

    def return_to_groups_page(self):
        # Return to group page
        self.app.set_minimum_wait_element_time()
        wd = self.app.wd
        if len(wd.find_elements_by_link_text('group page')) != 0:
            wd.find_element_by_link_text('group page').click()
        self.app.set_default_wait_element_time()

    def delete_all_groups(self):
        # Select all existing groups and delete them
        self.groups_page.select_all_groups()
        self.groups_page.click_delete_button()
        # Return to empty group page
        self.return_to_groups_page()

    def delete_selected_groups(self, groups_positions):
        # Select every group from list
        for position in groups_positions:
            self.groups_page.select_group(position)
        # Delete selected groups
        self.groups_page.click_delete_button()

    def update_selected_groups(self, groups_positions, group):
        # Select every group from list
        for position in groups_positions:
            self.groups_page.select_group(position)
        # Click edit group button
        self.groups_page.click_edit_group_button()
        # Fill group data
        if group is not None:
            self.group_edit_page.fill_group_page(group)
        else:
            # If group is null, just clear form
            self.group_edit_page.clear_new_group_form()
        # Confirm group creation
        self.group_edit_page.confirm_group_update()
        # Return to home page
        self.return_to_groups_page()

    def prepare_group_test_suite(self):
        self.open_groups_page()
        self.delete_all_groups()
