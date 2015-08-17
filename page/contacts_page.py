__author__ = 'Teo'


class ContactsPage:

    def __init__(self, app):
        self.app = app

    def click_delete_button(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        self.app.wd.switch_to_alert().accept()

    def click_edit_contact_button(self, contact_position):
        contact_position += 1
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr[" + str(contact_position) +
                                 "]/td[8]/a/img").click()

    def click_details_contact_button(self, contact_position):
        contact_position += 1
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr[" + str(contact_position) +
                                 "]/td[7]/a/img").click()

    def select_contact(self, contact_position):
        wd = self.app.wd
        # Select numbered contact
        contact_position += 1
        if not wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr["
                                                        + str(contact_position) + "]/td[1]/input").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr["
                                     + str(contact_position) + "]/td[1]/input").click()

    def select_all_contacts(self):
        wd = self.app.wd
        # Select all elements only if there are any rows in contact table
        if len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td")) > 1:
            if not wd.find_element_by_id("MassCB").is_selected():
                wd.find_element_by_id("MassCB").click()

    def click_new_contact_button(self):
        self.app.wd.find_element_by_link_text("add new").click()
