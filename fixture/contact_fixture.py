__author__ = 'Teo'
from page.new_contact_page import ContactEditPage
from page.contacts_page import ContactsPage
from page.contact_details_page import ContactDetailsPage
from model.contact_data import Contact


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
        self.contact_cache = None

    def return_to_home_page(self):
        # Don't click logo if we are already on main page
        wd = self.app.wd
        if not((len(wd.find_elements_by_link_text("Last name")) != 0) and
                (wd.current_url.endswith("/addressbook/"))):
            wd.find_element_by_id("logo").click()

    def delete_selected_contacts(self, contacts_positions):
        # Select every contact from list
        for position in contacts_positions:
            self.contacts_page.select_contact(position)
        # Delete selected contacts
        self.contacts_page.click_delete_button()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contacts_by_ids(self, contacts_ids):
        # Select every contact from list
        for contact_id in contacts_ids:
            self.contacts_page.select_contact_by_id(contact_id)
        # Delete selected contacts
        self.contacts_page.click_delete_button()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_from_update_page(self, contact_position):
        self.contacts_page.click_edit_contact_button(contact_position)
        self.new_contact_page.confirm_contact_delete()
        # Check contact
        self.return_to_home_page()
        self.contact_cache = None

    def update_contact_from_list_by_id(self, contact_id, contact):
        position = self.contacts_page.find_contact_position_by_id(contact_id)
        self.update_contact_from_list(position, contact)

    def update_contact_from_list(self, contact_position, contact):
        self.contacts_page.click_edit_contact_button(contact_position)
        # Fill contact data
        self.new_contact_page.fill_contact_data(contact)
        self.new_contact_page.confirm_contact_update()
        # Check contact
        self.return_to_home_page()
        self.contact_cache = None

    def update_contact_from_details_page(self, contact_position, contact):
        self.contacts_page.click_details_contact_button(contact_position)
        self.contact_detail.click_modify_button()
        # Fill contact data
        self.new_contact_page.fill_contact_data(contact)
        self.new_contact_page.confirm_contact_update()
        # Check contact
        self.return_to_home_page()
        self.contact_cache = None

    def delete_all_contacts(self):
        # Select all contacts
        self.contacts_page.select_all_contacts()
        # Delete it
        self.contacts_page.click_delete_button()
        self.return_to_home_page()
        self.contact_cache = None

    def prepare_contact_test_suite(self):
        # Delete all contacts
        self.delete_all_contacts()

    def count(self):
        self.return_to_home_page()
        return self.contacts_page.count_contacts()

    contact_cache = None

    def get_all_contacts(self):
        if self.contact_cache is None:
            self.return_to_home_page()
            self.contact_cache = []
            for element in self.contacts_page.get_all_contacts():
                # Get last name
                lastname = element.find_element_by_xpath("td[2]").text
                # Get first name
                firstname = element.find_element_by_xpath("td[3]").text
                # Get address
                address = element.find_element_by_xpath("td[4]").text
                # Get all emails
                all_emails = element.find_element_by_xpath("td[5]")
                email_list = []
                for one_href in all_emails.find_elements_by_xpath("a"):
                    email_list.append(one_href.text)
                # Get all phones
                all_phones = element.find_element_by_xpath("td[6]").text
                # Get id
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                temp_contact = Contact(firstname=firstname, lastname=lastname, id=contact_id)
                temp_contact.set_address(address)
                temp_contact.set_all_phones_from_home_page(all_phones_from_home_page=all_phones)
                temp_contact.set_all_emails_from_home_page(all_emails_from_home_page=email_list)
                self.contact_cache.append(temp_contact)
        return list(self.contact_cache)

    def check_if_contacts_are_equal(self, first_contacts, second_contacts):
        assert sorted(first_contacts, key=Contact.id_or_max) == sorted(second_contacts, key=Contact.id_or_max)

    def get_data_from_modification_page(self, contact_position):
        self.return_to_home_page()
        self.contacts_page.click_details_contact_button(contact_position)
        self.contact_detail.click_modify_button()
        # Fill contact data
        contact = self.new_contact_page.get_data_from_fields()
        # Check contact
        self.return_to_home_page()
        return contact

    def get_data_from_view_page(self, contact_position):
        self.return_to_home_page()
        self.contacts_page.click_details_contact_button(contact_position)
        # Fill contact data
        contact = self.contact_detail.get_contact_data()
        # Check contact
        self.return_to_home_page()
        return contact
