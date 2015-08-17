__author__ = 'Teo'


class ContactEditPage:

    def __init__(self, app):
        self.app = app

    def clear_new_contact_form(self):
        wd = self.app.wd
        # Clear primary contact data
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("homepage").clear()
        # Clear secondary contact data
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("notes").clear()
        # Clear birthday day elements
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        # Clear birthday month elements
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        # Clear birthday year
        wd.find_element_by_name("byear").clear()
        # Clear anniversary day elements
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[1]").click()
        # Clear anniversary month elements
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[1]").click()
        # Clear anniversary month elements
        wd.find_element_by_name("ayear").clear()

    def fill_primary_contact_data(self, contact):
        wd = self.app.wd
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
        if hasattr(contact, "nickname"):
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        if hasattr(contact, "title"):
            wd.find_element_by_name("title").send_keys(contact.title)
        # Fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        if hasattr(contact, "company"):
            wd.find_element_by_name("company").send_keys(contact.company)
        # Fill company address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        if hasattr(contact, "work_address"):
            wd.find_element_by_name("address").send_keys(contact.work_address)
        # Fill home phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        if hasattr(contact, "home_phone"):
            wd.find_element_by_name("home").send_keys(contact.home_phone)
        # Fill mobile phone number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        if hasattr(contact, "mobile_phone"):
            wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        # Fill work phone number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        if hasattr(contact, "work_phone"):
            wd.find_element_by_name("work").send_keys(contact.work_phone)
        # Fill fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        if hasattr(contact, "fax_phone"):
            wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        # Fill email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        if hasattr(contact, "first_email"):
            wd.find_element_by_name("email").send_keys(contact.first_email)
        # Fill second email
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        if hasattr(contact, "second_email"):
            wd.find_element_by_name("email2").send_keys(contact.second_email)
        # Fill third email
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        if hasattr(contact, "third_email"):
            wd.find_element_by_name("email3").send_keys(contact.third_email)
        # Fill home page
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        if hasattr(contact, "homepage"):
            wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def fill_secondary_contact_data(self, contact):
        wd = self.app.wd
        # Fill home address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        if hasattr(contact, "second_address"):
            wd.find_element_by_name("address2").send_keys(contact.second_address)
        # Fill home number
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        if hasattr(contact, "second_home"):
            wd.find_element_by_name("phone2").send_keys(contact.second_home)
        # Fill notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        if hasattr(contact, "second_notes"):
            wd.find_element_by_name("notes").send_keys(contact.second_notes)

    def fill_anniversary_data(self, contact):
        wd = self.app.wd
        # Fill anniversary day
        if hasattr(contact, "anniversary_day"):
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]").click()
        # Fill anniversary month
        if hasattr(contact, "anniversary_month"):
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]").click()
        # Fill anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        if hasattr(contact, "birthday_year"):
            wd.find_element_by_name("ayear").send_keys(contact.birthday_year)

    def fill_birthday_data(self, contact):
        wd = self.app.wd
        # Fill birthday day
        if hasattr(contact, "birthday_day"):
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]").click()
        # Fill birthday month
        if hasattr(contact, "birthday_month"):
            if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").is_selected():
                wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]").click()
        # Fill birthday year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        if hasattr(contact, "anniversary_year"):
            wd.find_element_by_name("byear").send_keys(contact.anniversary_year)

    def confirm_contact_creation(self):
        #self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.wd.find_element_by_name("submit").click()

    def confirm_contact_update(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()

    def confirm_contact_delete(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def fill_contact_data(self, contact):
        if contact != None:
            self.fill_primary_contact_data(contact)
            self.fill_secondary_contact_data(contact)
            self.fill_birthday_data(contact)
            self.fill_anniversary_data(contact)
        else:
            # If contact is null, just clear form
            self.clear_new_contact_form()