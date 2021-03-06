__author__ = 'Teo'
from model.contact_data import Contact
import random


def test_update_first_contact(app, db, check_ui):
    # Prepare before test
    app.contact.prepare_contact_test_suite()
    # Prepare old contact data
    contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation")
    contact.set_address(address="somewhere beyond the sea")
    contact.set_emails(first="ann.arner@megamailgroupofallworldcorporation.com",
                       second="ann@annhomemail.org", third="annnew@annhomemail.org")
    contact.set_homepage("www.somewherebeyondthesea.com")
    contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011",
                       second_phone="+123331212")
    contact.set_second_info(address="World 36", notes="She is my friend")
    contact.set_birthday(day="4", month="4", year="1987")
    contact.set_anniversary(day="31", month="7", year="2010")
    # Prepare new contact data
    new_contact = Contact(firstname="QAnny", middlename="QAA", lastname="QArnert", nickname="QTaT")
    new_contact.set_company_data(title="MegaMailGroutOfAllWorld2", company="MegaMailGroupOfAllWorldCorporation2")
    new_contact.set_address(address="somewhere beyond the sea2")
    new_contact.set_emails(first="ann.arner2@megamailgroupofallworldcorporation.com",
                           second="ann2@annhomemail.org", third="annnew2@annhomemail.org")
    new_contact.set_homepage("www.somewherebeyondthesea2.com")
    new_contact.set_phones(home="112223377", mobile="+7(000)9999911111777", work="44444477", fax="2300077",
                           second_phone="+1232461212")
    new_contact.set_second_info(address="World 77", notes="She is my best friend")
    new_contact.set_birthday(day="5", month="5", year="1986")
    new_contact.set_anniversary(day="12", month="3", year="2011")
    # Prepare other contacts
    second_contact = Contact(firstname="Dave", middlename="JD", lastname="Doe", nickname="Jay")
    # Create contacts
    app.contact.create(contact)
    app.contact.create(second_contact)
    old_contacts = app.contact.get_all_contacts()
    # Update contact
    new_contact.id = old_contacts[0].id
    app.contact.update_contact_from_list(1, new_contact)
    # Check contacts list
    old_contacts[0] = new_contact
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_update_middle_contact(app, db, check_ui):
    # Prepare before test
    app.contact.prepare_contact_test_suite()
    # Prepare old contact data
    contact = Contact(firstname="Dave", middlename="JD", lastname="Doe", nickname="Tee")
    contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation")
    contact.set_address(address="somewhere beyond the sea")
    contact.set_emails(first="ann.arner@megamailgroupofallworldcorporation.com",
                       second="ann@annhomemail.org", third="annnew@annhomemail.org")
    contact.set_homepage("www.somewherebeyondthesea.com")
    contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011",
                       second_phone="+123331212")
    contact.set_second_info(address="World 36", notes="She is my friend")
    contact.set_birthday(day="4", month="4", year="1987")
    contact.set_anniversary(day="31", month="7", year="2010")
    # Prepare new contact data
    new_contact = Contact(firstname="QAnny", middlename="QAA", lastname="QArnert", nickname="QTaT")
    new_contact.set_company_data(title="MegaMailGroutOfAllWorld2", company="MegaMailGroupOfAllWorldCorporation2")
    new_contact.set_address(address="somewhere beyond the sea2")
    new_contact.set_emails(first="ann.arner2@megamailgroupofallworldcorporation.com",
                           second="ann2@annhomemail.org", third="annnew2@annhomemail.org")
    new_contact.set_homepage("www.somewherebeyondthesea2.com")
    new_contact.set_phones(home="112223377", mobile="+7(000)9999911111777", work="44444477", fax="2300077",
                           second_phone="+1233399")
    new_contact.set_second_info(address="World 77", notes="She is my best friend")
    new_contact.set_birthday(day="5", month="5", year="1986")
    new_contact.set_anniversary(day="12", month="3", year="2011")
    # Prepare other contacts
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    # Create contacts
    app.contact.create(contact)
    app.contact.create(first_contact)
    app.contact.create(third_contact)
    old_contacts = app.contact.get_all_contacts()
    # Update contact
    new_contact.id = old_contacts[1].id
    app.contact.update_contact_from_list(2, new_contact)
    # Check contacts list
    old_contacts[1] = new_contact
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_update_last_contact(app, db, check_ui):
    # Prepare before test
    app.contact.prepare_contact_test_suite()
    # Prepare old contact data
    contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Tee")
    contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation")
    contact.set_address(address="somewhere beyond the sea")
    contact.set_emails(first="ann.arner@megamailgroupofallworldcorporation.com",
                       second="ann@annhomemail.org", third="annnew@annhomemail.org")
    contact.set_homepage("www.somewherebeyondthesea.com")
    contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011",
                       second_phone="+123331212")
    contact.set_second_info(address="World 36", notes="She is my friend")
    contact.set_birthday(day="4", month="4", year="1987")
    contact.set_anniversary(day="31", month="7", year="2010")
    # Prepare new contact data
    new_contact = Contact(firstname="Anny", middlename="AA", lastname="Arnert", nickname="TaT")
    new_contact.set_company_data(title="MegaMailGroutOfAllWorld2", company="MegaMailGroupOfAllWorldCorporation2")
    new_contact.set_address(address="somewhere beyond the sea2")
    new_contact.set_emails(first="ann.arner2@megamailgroupofallworldcorporation.com",
                           second="ann2@annhomemail.org", third="annnew2@annhomemail.org")
    new_contact.set_homepage("www.somewherebeyondthesea2.com")
    new_contact.set_phones(home="112223377", mobile="+7(000)9999911111777", work="44444477", fax="2300077",
                           second_phone="+111331212")
    new_contact.set_second_info(address="World 77", notes="She is my best friend")
    new_contact.set_birthday(day="5", month="5", year="1986")
    new_contact.set_anniversary(day="12", month="3", year="2011")
    # Prepare other contacts
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    # Create contacts
    app.contact.create(contact)
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    old_contacts = app.contact.get_all_contacts()
    # Update contact
    new_contact.id = old_contacts[2].id
    app.contact.update_contact_from_list(3, new_contact)
    # Check contacts list
    old_contacts[2] = new_contact
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_clear_contact_data(app, db, check_ui):
    # Prepare before test
    app.contact.prepare_contact_test_suite()
    # Prepare old contact data
    contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation")
    contact.set_address(address="somewhere beyond the sea")
    contact.set_emails(first="ann.arner@megamailgroupofallworldcorporation.com",
                       second="ann@annhomemail.org", third="annnew@annhomemail.org")
    contact.set_homepage("www.somewherebeyondthesea.com")
    contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011",
                       second_phone="+123331212")
    contact.set_second_info(address="World 36", notes="She is my friend")
    contact.set_birthday(day="4", month="4", year="1987")
    contact.set_anniversary(day="31", month="7", year="2010")
    # Create contacts
    app.contact.create(contact)
    old_contacts = db.get_contact_list()
    # Update contact
    new_contact = Contact("", "", "", "")
    new_contact.id = old_contacts[0].id
    app.contact.update_contact_from_list_by_id(new_contact.id, None)
    # Check contacts list
    old_contacts[0] = new_contact
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_update_contact_from_details_page(app, db, check_ui):
    # Prepare before test
    app.contact.prepare_contact_test_suite()
    # Prepare old contact data
    contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation")
    contact.set_address(address="somewhere beyond the sea")
    contact.set_emails(first="ann.arner@megamailgroupofallworldcorporation.com",
                       second="ann@annhomemail.org", third="annnew@annhomemail.org")
    contact.set_homepage("www.somewherebeyondthesea.com")
    contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011",
                       second_phone="+123331212")
    contact.set_second_info(address="World 36", notes="She is my friend")
    contact.set_birthday(day="4", month="4", year="1987")
    contact.set_anniversary(day="31", month="7", year="2010")
    # Create contacts
    app.contact.create(contact)
    old_contacts = app.contact.get_all_contacts()
    # Update contact
    app.contact.update_contact_from_details_page(1, None)
    new_contact = Contact("", "", "", "")
    new_contact.id = old_contacts[0].id
    # Check contacts list
    old_contacts[0] = new_contact
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_update_some_contact(app, db, check_ui):
    app.contact.set_default_contacts_view_on_contact_page()
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.update_contact_from_list_by_id(contact.id, None)
    # Count contacts
    new_contact = Contact("", "", "", "")
    new_contact.id = contact.id
    # Check contacts list
    old_contacts.remove(contact)
    old_contacts.append(new_contact)
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
