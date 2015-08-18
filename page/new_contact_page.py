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
        # Fill first name
        self.fill_string_field("firstname", contact.firstname)
        # Fill middle name
        self.fill_string_field("middlename", contact.middlename)
        # Fill last name
        self.fill_string_field("lastname", contact.lastname)
        # Fill nickname
        self.fill_string_field("nickname", contact.nickname)
        # Fill title
        self.fill_string_field("title", contact.title)
        # Fill company
        self.fill_string_field("company", contact.company)
        # Fill company address
        self.fill_string_field("address", contact.work_address)
        # Fill home phone number
        self.fill_string_field("home", contact.home_phone)
        # Fill mobile phone number
        self.fill_string_field("mobile", contact.mobile_phone)
        # Fill work phone number
        self.fill_string_field("work", contact.work_phone)
        # Fill fax
        self.fill_string_field("fax", contact.fax_phone)
        # Fill email
        self.fill_string_field("email", contact.first_email)
        # Fill second email
        self.fill_string_field("email2", contact.second_email)
        # Fill third email
        self.fill_string_field("email3", contact.third_email)
        # Fill home page
        self.fill_string_field("homepage", contact.homepage)

    def fill_secondary_contact_data(self, contact):
        # Fill home address
        self.fill_string_field("address2", contact.second_address)
        # Fill home number
        self.fill_string_field("phone2", contact.second_home)
        # Fill notes
        self.fill_string_field("notes", contact.second_notes)

    def fill_anniversary_data(self, contact):
        wd = self.app.wd
        # Fill anniversary day
        if contact.anniversary_day is not None:
            anniversary_day_xpath = "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]"
            if not wd.find_element_by_xpath(anniversary_day_xpath).is_selected():
                wd.find_element_by_xpath(anniversary_day_xpath).click()
        # Fill anniversary month
        if contact.anniversary_month is not None:
            anniversary_month_xpath = "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]"
            if not wd.find_element_by_xpath(anniversary_month_xpath).is_selected():
                wd.find_element_by_xpath(anniversary_month_xpath).click()
        # Fill anniversary year
        self.fill_string_field("ayear", contact.anniversary_year)

    def fill_birthday_data(self, contact):
        wd = self.app.wd
        # Fill birthday day
        if contact.birthday_day is not None:
            birthday_day_xpath = "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]"
            if not wd.find_element_by_xpath(birthday_day_xpath).is_selected():
                wd.find_element_by_xpath(birthday_day_xpath).click()
        # Fill birthday month
        if contact.birthday_month is not None:
            birthday_month_xpath = "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]"
            if not wd.find_element_by_xpath(birthday_month_xpath).is_selected():
                wd.find_element_by_xpath(birthday_month_xpath).click()
        # Fill birthday year
        self.fill_string_field("byear", contact.birthday_year)

    def confirm_contact_creation(self):
        self.app.wd.find_element_by_name("submit").click()

    def confirm_contact_update(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()

    def confirm_contact_delete(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def fill_contact_data(self, contact):
        if contact is not None:
            self.fill_primary_contact_data(contact)
            self.fill_secondary_contact_data(contact)
            self.fill_birthday_data(contact)
            self.fill_anniversary_data(contact)
        else:
            # If contact is null, just clear form
            self.clear_new_contact_form()

    def fill_string_field(self, field_name, new_value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).clear()
        if new_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).send_keys(new_value)
