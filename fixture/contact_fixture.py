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
