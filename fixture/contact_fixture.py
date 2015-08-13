__author__ = 'Teo'
from page.new_contact_page import ContactPage


class ContactUtils:

    def __init__(self, app):
        self.app = app
        self.contact_page = ContactPage(app)

    def create(self, contact):
        # Open new contact page
        self.open_new_contact_page()
        # Fill contact data
        if contact != None:
            self.contact_page.fill_primary_contact_data(contact)
            self.contact_page.fill_secondary_contact_data(contact)
            self.contact_page.fill_birthday_data(contact)
            self.contact_page.fill_anniversary_data(contact)
        else:
            # If contact is null, just clear form
            self.contact_page.clear_new_contact_form()
        self.contact_page.confirm_contact_creation()
        # Check contact
        self.return_to_home_page()

    def return_to_home_page(self):
        self.app.wd.find_element_by_link_text("home page").click()

    def open_new_contact_page(self):
        self.app.wd.find_element_by_link_text("add new").click()

    def delete(self, contact_position):
        wd = self.app.wd
        # Select numbered contact
        contact_position += 1
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/table/tbody/tr[" + contact_position +
                                 "]/td[0]/input").click()
        # Delete it
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        # return to home page
        wd.switch_to_alert().accept()


    def delete_all_contacts(self):
        wd = self.app.wd
        # Select numbered contact
        if not wd.find_element_by_id("MassCB").is_selected():
            wd.find_element_by_id("MassCB").click()
        # Delete it
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        # return to home page
        wd.switch_to_alert().accept()
