__author__ = 'Teo'
from page.new_group_page import GroupEditPage
from page.groups_page import GroupsPage
from model.group_data import Group


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
        self.group_cache = None

    def open_groups_page(self):
        # Open groups page
        wd = self.app.wd
        if not ((len(wd.find_elements_by_name("new")) != 0) and (wd.current_url.endswith("/group.php"))):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        # Return to group page
        wd = self.app.wd
        if not ((len(wd.find_elements_by_name("new")) != 0) and (wd.current_url.endswith("/group.php"))):
            wd.find_element_by_link_text("group page").click()

    def delete_all_groups(self):
        self.open_groups_page()
        # Select all existing groups and delete them
        self.groups_page.select_all_groups()
        self.groups_page.click_delete_button()
        # Return to empty group page
        self.return_to_groups_page()
        self.group_cache = None

    def delete_selected_groups(self, groups_positions):
        self.open_groups_page()
        # Select every group from list
        for position in groups_positions:
            self.groups_page.select_group(position)
        # Delete selected groups
        self.groups_page.click_delete_button()
        self.group_cache = None

    def delete_groups_by_ids(self, id_list):
        self.open_groups_page()
        # Select every group from list
        for group_id in id_list:
            self.groups_page.select_group_by_id(group_id)
        # Delete selected groups
        self.groups_page.click_delete_button()
        self.group_cache = None

    def update_groups_by_ids(self, id_list, group):
        self.open_groups_page()
        # Select every group from list
        for group_id in id_list:
            self.groups_page.select_group_by_id(group_id)
        self.update_group_after_selection(group)

    def update_selected_groups(self, groups_positions, group):
        self.open_groups_page()
        # Select every group from list
        for position in groups_positions:
            self.groups_page.select_group(position)
        self.update_group_after_selection(group)

    def update_group_after_selection(self, group):
        self.open_groups_page()
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
        self.group_cache = None

    def prepare_group_test_suite(self):
        self.open_groups_page()
        self.delete_all_groups()

    def count(self):
        self.open_groups_page()
        return self.groups_page.count_groups()

    group_cache = None

    def get_all_groups(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.groups_page.get_all_groups():
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))
        return list(self.group_cache)

    def check_if_groups_are_equal(self, first_groups, second_groups):
        assert sorted(first_groups, key=Group.id_or_max) == sorted(second_groups, key=Group.id_or_max)
