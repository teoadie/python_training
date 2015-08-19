__author__ = 'Teo'


class ContactDetailsPage:

    def __init__(self, app):
        self.app = app

    def click_modify_button(self):
        wd = self.app.wd
        wd.find_element_by_name("modifiy").click()
