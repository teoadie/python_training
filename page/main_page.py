__author__ = 'Teo'


class MainPage:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # open home page
        self.app.wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        # Fill login field
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(username)
        # Fill password field
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(password)
        # Confirm login
        self.app.wd.find_element_by_css_selector("input[type=\'submit\']").click()

    def login_as_admin(self):
        self.login("admin", "secret")

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as_user(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_login_as_admin(self):
        self.ensure_login("admin", "secret")

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        self.app.set_minimum_waiting_period()
        check_result = len(self.app.wd.find_elements_by_link_text("Logout")) > 0
        self.app.set_default_waiting_period()
        return check_result

    def is_logged_in_as_user(self, username):
        current_login = self.app.wd.find_element_by_xpath("//div/div[1]/form/b").text
        return current_login == "(" + username + ")"
