# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from function import main_page
from model.contact_data import Contact

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
        contact = Contact(firstname="Ann", middlename="AT", lastname="Terner", nickname="Tee" )
        contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation",
                                 address="somewhere beyond the sea")
        contact.set_emails(first="ann.terner@megamailgroupofallworldcorporation.com",
                           second="ann@annhomemail.org", third="annnew@annhomemail.org")
        contact.set_homepage("www.somewherebeyondthesea.com")
        contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011")
        contact.set_second_info(address="World 36", home="77", notes="She is my friend")
        # Create new contact
        self.add_new_contact(wd)
        self.fill_primary_contact_data(wd, contact)
        self.fill_secondary_contact_data(wd, contact)
        self.fill_birthday_data(wd)
        self.fill_anniversary_data(wd)
        self.submit_contact(wd)
        # Check contact
        self.return_to_home_page(wd)
        main_page.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        # Create new contact
        self.add_new_contact(wd)
        self.submit_contact(wd)
        # Check contact
        self.return_to_home_page(wd)
        main_page.logout(wd)

    def test_add_contact_without_second_info(self):
        wd = self.wd
        main_page.open_home_page(wd)
        main_page.login_as_admin(wd)
        # Create new contact and fill its data
        contact = Contact(firstname="Ann", middlename="AT", lastname="Terner", nickname="Tee" )
        contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation",
                                 address="somewhere beyond the sea")
        contact.set_emails(first="ann.terner@megamailgroupofallworldcorporation.com",
                           second="ann@annhomemail.org", third="annnew@annhomemail.org")
        contact.set_homepage("www.somewherebeyondthesea.com")
        contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011")
        # Create new contact
        self.add_new_contact(wd)
        self.fill_primary_contact_data(wd, contact)
        self.fill_birthday_data(wd)
        self.fill_anniversary_data(wd)
        self.submit_contact(wd)
        # Check contact
        self.return_to_home_page(wd)
        main_page.logout(wd)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def submit_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fill_primary_contact_data(self, wd, contact):
        # Fill first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # Fill middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # Fill last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # Fill nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # Fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # Fill company address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.work_address)
        # Fill home phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # Fill mobile phone number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        # Fill work phone number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        # Fill fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        # Fill email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.first_email)
        # Fill second email
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.second_email)
        # Fill third email
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.third_email)
        # Fill home page
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def fill_secondary_contact_data(self, wd, contact):
        # Fill home address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.second_address)
        # Fill home number
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.second_home)
        # Fill notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.second_notes)

    def fill_anniversary_data(self, wd):
        # Fill anniversary day
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[12]").click()
        # Fill anniversary month
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[8]").click()
        # Fill anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2010")

    def fill_birthday_data(self, wd):
        # Fill birthday day
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        # Fill birthday month
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        # Fill birthday year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1988")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
