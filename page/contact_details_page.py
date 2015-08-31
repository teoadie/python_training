__author__ = 'Teo'
import re
from model.contact_data import Contact


class ContactDetailsPage:

    def __init__(self, app):
        self.app = app

    def click_modify_button(self):
        wd = self.app.wd
        wd.find_element_by_name("modifiy").click()

    def get_contact_data(self):
        wd = self.app.wd
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        new_contact = Contact()
        new_contact.set_phones(home=home_phone, mobile=mobile_phone, work=work_phone, second_phone=secondary_phone,
                               fax=None)
        return new_contact
