__author__ = 'Teo'


def clear_new_group_form(wd):
    wd.find_element_by_name('group_name').clear()
    wd.find_element_by_name('group_header').clear()
    wd.find_element_by_name('group_footer').clear()


def fill_group_page(wd, group):
    wd.find_element_by_name('group_name').click()
    wd.find_element_by_name('group_name').clear()
    wd.find_element_by_name('group_name').send_keys(group.name)
    wd.find_element_by_name('group_header').click()
    wd.find_element_by_name('group_header').clear()
    wd.find_element_by_name('group_header').send_keys(group.header)
    wd.find_element_by_name('group_footer').click()
    wd.find_element_by_name('group_footer').clear()
    wd.find_element_by_name('group_footer').send_keys(group.footer)


def confirm_group_creation(wd):
    wd.find_element_by_name('submit').click()
