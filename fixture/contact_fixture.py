__author__ = 'Teo'
from page.new_contact_page import ContactEditPage
from page.contacts_page import ContactsPage
from page.contact_details_page import ContactDetailsPage


class ContactUtils:

    def __init__(self, app):
        self.app = app
        self.new_contact_page = ContactEditPage(app)
        self.contacts_page = ContactsPage(app)
        self.contact_detail = ContactDetailsPage(app)

    def create(self, contact):
        # Open new contact page
        self.contacts_page.click_new_contact_button()
        # Fill contact data
        self.new_contact_page.fill_contact_data(contact)
        self.new_contact_page.confirm_contact_creation()
        # Check contact
        self.return_to_home_page()

    def return_to_home_page(self):
        # Don't click logo if we are already on main page
        self.app.set_minimum_waiting_period()
        wd = self.app.wd
        if not((len(wd.find_elements_by_link_text("Last name")) != 0) and
                (wd.current_url.endswith("/addressbook/"))):
            wd.find_element_by_id("logo").click()
        self.app.set_default_waiting_period()

    def delete_selected_contacts(self, contacts_positions):
        # Select every contact from list
        for position in contacts_positions:
            self.contacts_page.select_contact(position)
        # Delete selected contacts
        self.contacts_page.click_delete_button()
        self.return_to_home_page()

    def delete_contact_from_update_page(self, contact_position):
        self.contacts_page.click_edit_contact_button(contact_position)
        self.new_contact_page.confirm_contact_delete()
        # Check contact
        self.return_to_home_page()

    def update_contact_from_list(self, contact_position, contact):
        self.contacts_page.click_edit_contact_button(contact_position)
        # Fill contact data
        self.new_contact_page.fill_contact_data(contact)
        self.new_contact_page.confirm_contact_update()
        # Check contact
        self.return_to_home_page()

    def update_contact_from_details_page(self, contact_position, contact):
        self.contacts_page.click_details_contact_button(contact_position)
        self.contact_detail.click_modify_button()
        # Fill contact data
        self.new_contact_page.fill_contact_data(contact)
        self.new_contact_page.confirm_contact_update()
        # Check contact
        self.return_to_home_page()

    def delete_all_contacts(self):
        # Select all contacts
        self.contacts_page.select_all_contacts()
        # Delete it
        self.contacts_page.click_delete_button()
        self.return_to_home_page()

    def prepare_contact_test_suite(self):
        # Delete all contacts
        self.delete_all_contacts()
