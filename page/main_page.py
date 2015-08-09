__author__ = 'Teo'


class MainPage:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # open home page
        self.app.wd.get('http://localhost/addressbook/')

    def login(self, username, password):
        self.open_home_page()
        # Fill login field
        self.app.wd.find_element_by_name('user').click()
        self.app.wd.find_element_by_name('user').clear()
        self.app.wd.find_element_by_name('user').send_keys(username)
        # Fill password field
        self.app.wd.find_element_by_name('pass').click()
        self.app.wd.find_element_by_name('pass').clear()
        self.app.wd.find_element_by_name('pass').send_keys(password)
        # Confirm login
        self.app.wd.find_element_by_css_selector('input[type=\'submit\']').click()

    def login_as_admin(self):
        self.login('admin', 'secret')

    def logout(self):
        # Logout
        self.app.wd.find_element_by_link_text('Logout').click()
