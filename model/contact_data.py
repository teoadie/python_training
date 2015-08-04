__author__ = 'Teo'


class Contact:

    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname

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

