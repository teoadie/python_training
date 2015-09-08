__author__ = 'Teo'


class MainPage:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def login(self, username, password):
        wd = self.app.wd
        self.open_home_page()
        # Fill login field
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        # Fill password field
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # Confirm login
        wd.find_element_by_css_selector("input[type='submit']").click()

    def login_as_default_user(self):
        self.login(self.app.default_login, self.app.default_password)

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as_user(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_login_by_default_user(self):
        self.ensure_login(self.app.default_login, self.app.default_password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        check_result = len(wd.find_elements_by_link_text("Logout")) > 0
        return check_result

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def is_logged_in_as_user(self, username):
        return self.get_logged_user() == username
