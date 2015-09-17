__author__ = 'Teo'
from model.contact_data import Contact


def test_check_random_contact_on_main_page(app):
    if app.contact.count() == 0:
        contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
        contact.set_phones(home="3321123", mobile="+792938232", work="44142221", second_phone="+791229313", fax="2123")
        app.contact.create(contact)
    contact_from_main_page = app.contact.get_all_contacts()[0]
    contact_from_edit_page = app.contact.get_data_from_modification_page(1)
    # Check last name
    assert check_if_home_page_value_equal_to_contact_value(contact_from_main_page.lastname,
                                                           contact_from_edit_page.lastname)
    # Check first name
    assert check_if_home_page_value_equal_to_contact_value(contact_from_main_page.firstname,
                                                           contact_from_edit_page.firstname)
    # Check address
    assert check_if_home_page_value_equal_to_contact_value(contact_from_main_page.address,
                                                           contact_from_edit_page.address)
    # Check emails
    assert contact_from_main_page.all_emails_from_home_page == contact_from_edit_page.merge_emails_like_on_home_page()
    # Check phone numbers
    assert contact_from_main_page.all_phones_from_home_page == contact_from_edit_page.merge_phones_like_on_home_page()


def check_if_home_page_value_equal_to_contact_value(home_page_data, contact_data):
    if home_page_data == contact_data:
        return True
    if home_page_data == "":
        if contact_data == "" or contact_data == " ":
            return True
    return False
