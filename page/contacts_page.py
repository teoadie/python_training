__author__ = 'Teo'


class ContactsPage:

    def __init__(self, app):
        self.app = app

    def click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        wd.switch_to_alert().accept()

    def click_edit_contact_button(self, contact_position):
        wd = self.app.wd
        contact_position += 1
        xpath = "//div[@id='content']/form[@name='MainForm']/table/tbody/tr[%s]/td[8]/a/img" % str(contact_position)
        wd.find_element_by_xpath(xpath).click()

    def click_details_contact_button(self, contact_position):
        wd = self.app.wd
        contact_position += 1
        xpath = "//div[@id='content']/form[@name='MainForm']/table/tbody/tr[%s]/td[7]/a/img" % str(contact_position)
        wd.find_element_by_xpath(xpath).click()

    def find_contact_position_by_id(self, contact_id):
        wd = self.app.wd
        count_contacts = self.count_contacts()
        if count_contacts != 0:
            for position in range (2, count_contacts + 2):
                xpath = "//div[@id='content']/form[@name='MainForm']/table/tbody/tr[%s]/td[1]/input[@id='%s']" \
                          % (str(position), str(contact_id))
                try:
                    element = wd.find_element_by_xpath(xpath)
                    if element is not None:
                        return position - 1
                except:
                    pass
        raise ValueError('Contact with id %s not found on main page' % str(contact_id))

    def select_contact(self, contact_position):
        wd = self.app.wd
        # Select numbered contact
        contact_position += 1
        xpath = "//div[@id='content']/form[@name='MainForm']/table/tbody/tr[%s]/td[1]/input" % str(contact_position)
        if not wd.find_element_by_xpath(xpath).is_selected():
            wd.find_element_by_xpath(xpath).click()

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        # Select numbered contact
        css_selector = "input[value='%s']" % str(contact_id)
        wd.find_element_by_css_selector(css_selector).click()
        #xpath = "//div[@id='content']/form[@name='MainForm']/table/tbody/tr/td[1]/input[id='%s']" % str(contact_id)
        #if not wd.find_element_by_xpath(xpath).is_selected():
        #    wd.find_element_by_xpath(xpath).click()

    def select_all_contacts(self):
        wd = self.app.wd
        # Select all elements only if there are any rows in contact table
        if len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td")) > 1:
            if not wd.find_element_by_id("MassCB").is_selected():
                wd.find_element_by_id("MassCB").click()

    def click_new_contact_button(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count_contacts(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("entry"))

    def get_all_contacts(self):
        wd = self.app.wd
        return wd.find_elements_by_name("entry")
