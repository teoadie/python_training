__author__ = 'Teo'
from sys import maxsize
import re


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.title = None
        self.company = None
        self.address = None
        self.home_phone = None
        self.mobile_phone = None
        self.work_phone = None
        self.fax_phone = None
        self.first_email = None
        self.second_email = None
        self.third_email = None
        self.homepage = None
        self.second_address = None
        self.second_phone = None
        self.second_notes = None
        self.birthday_day = None
        self.birthday_month = None
        self.birthday_year = None
        self.anniversary_day = None
        self.anniversary_month = None
        self.anniversary_year = None
        self.all_phones_from_home_page = None
        self.all_emails_from_home_page = None

    def set_company_data(self, title, company):
        self.title = title
        self.company = company

    def set_address(self, address):
        self.address = address

    def set_phones(self, home, mobile, work, fax, second_phone):
        self.home_phone = home
        self.mobile_phone = mobile
        self.work_phone = work
        self.fax_phone = fax
        self.second_phone = second_phone

    def set_emails(self, first, second, third):
        self.first_email = first
        self.second_email = second
        self.third_email = third

    def set_homepage(self, homepage):
        self.homepage = homepage

    def set_second_info(self, address, notes):
        self.second_address = address
        self.second_notes = notes

    def set_birthday(self, day, month, year):
        self.birthday_day = day
        self.birthday_month = month
        self.birthday_year = year

    def set_anniversary(self, day, month, year):
        self.anniversary_day = day
        self.anniversary_month = month
        self.anniversary_year = year

    def set_all_phones_from_home_page(self, all_phones_from_home_page):
        self.all_phones_from_home_page = all_phones_from_home_page

    def set_all_emails_from_home_page(self, all_emails_from_home_page):
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        if self.lastname == other.lastname and self.firstname == other.firstname:
            if self.id is None or other.id is None or self.id == other.id:
                return True
        return False

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def merge_phones_like_on_home_page(self):
        return "\n".join(filter(lambda y: y != "",
                                map(lambda x: self.clear_not_used_phone_symbols(x),
                                    filter(lambda z: z is not None, [self.home_phone,
                                                                     self.work_phone,
                                                                     self.mobile_phone,
                                                                     self.second_phone]))))

    def merge_emails_like_on_home_page(self):
        all_emails = []
        if self.is_email_filled_in_home_page(self.first_email):
            all_emails.append(self.first_email)
        if self.is_email_filled_in_home_page(self.second_email):
            all_emails.append(self.second_email)
        if self.is_email_filled_in_home_page(self.third_email):
            all_emails.append(self.third_email)
        return all_emails

    def is_email_filled_in_home_page(self, email):
        return email is not None and email != "" and email != " "

    def clear_not_used_phone_symbols(self, phone_number):
        return re.sub("[() -]", "", phone_number)
