from selenium.common.exceptions import NoSuchElementException

__author__ = 'Teo'


class GroupsPage:

    def __init__(self, app):
        self.app = app

    def click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def click_edit_group_button(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def select_group(self, group_position):
        wd = self.app.wd
        # Select numbered group
        xpath = "//div[@id='content']/form/span[%s]/input" % str(group_position)
        wd.find_element_by_xpath(xpath).click()

    def select_group_by_id(self, group_id):
        wd = self.app.wd
        # Select numbered group
        css_selector = "input[value='%s']" % str(group_id)
        wd.find_element_by_css_selector(css_selector).click()

    def select_all_groups(self):
        wd = self.app.wd
        # Select all groups
        if len(wd.find_elements_by_name("selected[]")) != 0:
            all_groups = wd.find_elements_by_name("selected[]")
            for one_group_row in all_groups:
                if not one_group_row.is_selected():
                    one_group_row.click()

    def click_new_group_button(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def count_groups(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_all_groups(self):
        wd = self.app.wd
        return wd.find_elements_by_css_selector("span.group")
