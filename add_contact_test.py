# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver
from pages import main_page
from model.contact_data import Contact
from pages import new_contact_page


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class add_contact_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        # Create new contact and fill its data
        contact = Contact(firstname="Ann", middlename="AT", lastname="Terner", nickname="Tee")
        contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation",
                                 address="somewhere beyond the sea")
        contact.set_emails(first="ann.terner@megamailgroupofallworldcorporation.com",
                           second="ann@annhomemail.org", third="annnew@annhomemail.org")
        contact.set_homepage("www.somewherebeyondthesea.com")
        contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011")
        contact.set_second_info(address="World 36", home="77", notes="She is my friend")
        contact.set_birthday(day="4", month="4", year="1987")
        contact.set_anniversary(day="31", month="7", year="2010")
        # Create new contact
        self.add_new_contact(wd)
        # Clear form
        new_contact_page.clear_new_contact_form(wd)
        # Fill form with data
        new_contact_page.fill_primary_contact_data(wd, contact)
        new_contact_page.fill_secondary_contact_data(wd, contact)
        new_contact_page.fill_birthday_data(wd, contact)
        new_contact_page.fill_anniversary_data(wd, contact)
        new_contact_page.confirm_contact_creation(wd)
        # Check contact
        self.return_to_home_page(wd)
        main_page.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        # Create new contact
        self.add_new_contact(wd)
        # Clear form
        new_contact_page.clear_new_contact_form(wd)
        # Confirm contract data
        new_contact_page.confirm_contact_creation(wd)
        # Check contact
        self.return_to_home_page(wd)
        main_page.logout(wd)

    def test_add_contact_with_spaces_in_fields(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        # Create new contact and fill its data
        contact = Contact(firstname=" ", middlename=" ", lastname=" ", nickname=" ")
        contact.set_company_data(title=" ", company=" ", address=" ")
        contact.set_emails(first=" ", second=" ", third=" ")
        contact.set_homepage(" ")
        contact.set_phones(home=" ", mobile=" ", work=" ", fax=" ")
        contact.set_second_info(address=" ", home=" ", notes=" ")
        contact.set_birthday(day="1", month="1", year=" ")
        contact.set_anniversary(day="1", month="1", year=" ")
        # Create new contact
        self.add_new_contact(wd)
        # Clear form
        new_contact_page.clear_new_contact_form(wd)
        # Fill form with data
        new_contact_page.fill_primary_contact_data(wd, contact)
        new_contact_page.fill_secondary_contact_data(wd, contact)
        new_contact_page.fill_birthday_data(wd, contact)
        new_contact_page.fill_anniversary_data(wd, contact)
        new_contact_page.confirm_contact_creation(wd)
        # Check contact
        self.return_to_home_page(wd)
        main_page.logout(wd)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
