__author__ = 'Teo'
from sys import maxsize
import re


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None, title=None,
                 company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None,
                 first_email=None, second_email=None, third_email=None, homepage=None, second_address=None,
                 second_phone=None, second_notes=None, birthday_day=None, birthday_month=None, birthday_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.first_email = first_email
        self.second_email = second_email
        self.third_email = third_email
        self.homepage = homepage
        self.second_address = second_address
        self.second_phone = second_phone
        self.second_notes = second_notes
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
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
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        if self.check_two_fields(self.lastname, other.lastname) and \
                self.check_two_fields(self.firstname, other.firstname):
            if self.id is None or other.id is None or self.id == other.id:
                return True
        return False

    def check_two_fields(self, first_field, second_field):
        if (first_field == second_field) or\
                (first_field == "" and second_field == " ") or\
                (first_field == " " and second_field == "") :
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
