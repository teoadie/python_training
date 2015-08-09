__author__ = 'Teo'
from selenium.webdriver.firefox.webdriver import WebDriver
from pages import new_contact_page
from pages import main_page

class ContactFixture:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def destroy(self):
        self.wd.quit()

    def open_contact_page_and_create_new_contact(self,contact):
        wd = self.wd
        # Open new contact page
        self.add_new_contact()
        # Fill contact data
        if contact != None:
            new_contact_page.fill_primary_contact_data(wd, contact)
            new_contact_page.fill_secondary_contact_data(wd, contact)
            new_contact_page.fill_birthday_data(wd, contact)
            new_contact_page.fill_anniversary_data(wd, contact)
        else:
            # If contact is null, just clear form
            new_contact_page.clear_new_contact_form(wd)
        new_contact_page.confirm_contact_creation(wd)
        # Check contact
        self.return_to_home_page()

    def return_to_home_page(self):
        self.wd.find_element_by_link_text("home page").click()

    def add_new_contact(self):
        self.wd.find_element_by_link_text("add new").click()

    def logout(self):
        # Return to login page
        main_page.logout(self.wd)

    def login(self):
        wd = self.wd
        # Open home page
        main_page.open_home_page(wd)
        # Login by admin
        main_page.login_as_admin(wd)
