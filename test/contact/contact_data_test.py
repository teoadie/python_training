__author__ = 'Teo'
from model.contact_data import Contact


def test_check_all_contacts_on_main_page(app, db):
    if app.contact.count() == 0:
        contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
        contact.set_phones(home="3321123", mobile="+792938232", work="44142221", second_phone="+791229313", fax="2123")
        app.contact.create(contact)
    contacts_from_main_page = app.contact.get_all_contacts()
    contacts_from_db = db.get_contact_list()
    for db_contact in contacts_from_db:
        value_found = False
        for web_contact in contacts_from_main_page:
            if db_contact.id == web_contact.id:
                value_found = True
                check_all_values_on_home_page(web_contact, db_contact)
                break
        if not value_found:
            raise ValueError('Contact with id %s not found on main page' % str(db_contact.id))


def check_all_values_on_home_page(contact_from_main_page, db_contact_data):
    # Check last name
    assert check_if_home_page_value_equal_to_contact_value(contact_from_main_page.lastname,
                                                           db_contact_data.lastname)
    # Check first name
    assert check_if_home_page_value_equal_to_contact_value(contact_from_main_page.firstname,
                                                           db_contact_data.firstname)
    # Check address
    assert check_if_home_page_value_equal_to_contact_value(contact_from_main_page.address,
                                                           db_contact_data.address)
    # Check emails
    assert contact_from_main_page.all_emails_from_home_page == db_contact_data.merge_emails_like_on_home_page()
    # Check phone numbers
    assert contact_from_main_page.all_phones_from_home_page == db_contact_data.merge_phones_like_on_home_page()


def check_if_home_page_value_equal_to_contact_value(home_page_data, contact_data):
    if home_page_data == contact_data:
        return True
    if home_page_data == "":
        if contact_data == "" or contact_data == " " or contact_data is None:
            return True
    return False
