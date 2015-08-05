__author__ = 'Teo'


def open_home_page(wd):
    # open home page
    wd.get('http://localhost/addressbook/')


def login(wd, username, password):
    # Fill login field
    wd.find_element_by_name('user').click()
    wd.find_element_by_name('user').clear()
    wd.find_element_by_name('user').send_keys(username)
    # Fill password field
    wd.find_element_by_name('pass').click()
    wd.find_element_by_name('pass').clear()
    wd.find_element_by_name('pass').send_keys(password)
    # Confirm login
    wd.find_element_by_css_selector('input[type=\'submit\']').click()


def login_as_admin(wd):
    login(wd, 'admin', 'secret')


def logout(wd):
    # Logout
    wd.find_element_by_link_text('Logout').click()
