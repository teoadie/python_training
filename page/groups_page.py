from selenium.common.exceptions import NoSuchElementException

__author__ = 'Teo'


class GroupsPage:

    def __init__(self, app):
        self.app = app

    def click_delete_button(self):
        self.app.wd.find_element_by_name("delete").click()

    def click_edit_group_button(self):
        self.app.wd.find_element_by_name("edit").click()

    def select_group(self, group_position):
        wd = self.app.wd
        # Select numbered group
        wd.find_element_by_xpath("//div[@id='content']/form/span[" + str(group_position) + "]/input").click()

    def select_all_groups(self):
        wd = self.app.wd
        # Select all groups
        self.app.set_minimum_waiting_period()
        if (len(wd.find_elements_by_name("selected[]")) != 0):
            all_groups = wd.find_elements_by_name("selected[]")
            for one_group_row in all_groups:
                if not one_group_row.is_selected():
                    one_group_row.click()
        self.app.set_default_waiting_period()

    def click_new_group_button(self):
        self.app.wd.find_element_by_name("new").click()
