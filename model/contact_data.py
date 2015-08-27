__author__ = 'Teo'


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = None
        self.company = None
        self.work_address = None
        self.home_phone = None
        self.mobile_phone = None
        self.work_phone = None
        self.fax_phone = None
        self.first_email = None
        self.second_email = None
        self.third_email = None
        self.homepage = None
        self.second_address = None
        self.second_home = None
        self.second_notes = None
        self.birthday_day = None
        self.birthday_month = None
        self.birthday_year = None
        self.anniversary_day = None
        self.anniversary_month = None
        self.anniversary_year = None

    def set_company_data(self, title, company, address):
        self.title = title
        self.company = company
        self.work_address = address

    def set_phones(self, home, mobile, work, fax):
        self.home_phone = home
        self.mobile_phone = mobile
        self.work_phone = work
        self.fax_phone = fax

    def set_emails(self, first, second, third):
        self.first_email = first
        self.second_email = second
        self.third_email = third

    def set_homepage(self, homepage):
        self.homepage = homepage

    def set_second_info(self, address, home, notes):
        self.second_address = address
        self.second_home = home
        self.second_notes = notes

    def set_birthday(self, day, month, year):
        self.birthday_day = day
        self.birthday_month = month
        self.birthday_year = year

    def set_anniversary(self, day, month, year):
        self.anniversary_day = day
        self.anniversary_month = month
        self.anniversary_year = year
