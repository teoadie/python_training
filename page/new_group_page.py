__author__ = 'Teo'


class GroupEditPage:

    def __init__(self, app):
        self.app = app

    def clear_new_group_form(self):
        wd = self.app.wd
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_footer").clear()

    def fill_group_page_by_group_object(self, group):
        self.fill_string_field("group_name", group.name)
        self.fill_string_field("group_header", group.header)
        self.fill_string_field("group_footer", group.footer)

    def confirm_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def confirm_group_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def fill_group_page(self, group):
        # Fill group data
        if group is not None:
            self.fill_group_page_by_group_object(group)
        else:
            # If group is null, just clear form
            self.clear_new_group_form()

    def fill_string_field(self, field_name, new_value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).clear()
        if new_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).send_keys(new_value)
