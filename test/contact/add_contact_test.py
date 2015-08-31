# -*- coding: utf-8 -*-
from model.contact_data import Contact


def test_add_contact(app):
    # Create new contact object and fill its data
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
    app.contact.prepare_contact_test_suite()
    old_contacts = app.contact.get_all_contacts()
    # Create new contact
    app.contact.create(contact)
    # Count contacts
    assert len(old_contacts) + 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts.append(contact)
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_add_empty_contact(app):
    app.contact.prepare_contact_test_suite()
    old_contacts = app.contact.get_all_contacts()
    # Create new contact
    app.contact.create(None)
    # Count contacts
    assert len(old_contacts) + 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts.append(Contact("", "", "", ""))
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_add_contact_with_spaces_in_fields(app):
    # Create new contact object and fill its data
    contact = Contact(firstname=" ", middlename=" ", lastname=" ", nickname=" ")
    contact.set_company_data(title=" ", company=" ")
    contact.set_address(address=" ")
    contact.set_emails(first=" ", second=" ", third=" ")
    contact.set_homepage(" ")
    contact.set_phones(home=" ", mobile=" ", work=" ", fax=" ", second_phone=" ")
    contact.set_second_info(address=" ", notes=" ")
    contact.set_birthday(day="1", month="1", year=" ")
    contact.set_anniversary(day="1", month="1", year=" ")
    app.contact.prepare_contact_test_suite()
    old_contacts = app.contact.get_all_contacts()
    # Create new contact
    app.contact.create(contact)
    # Count contacts
    assert len(old_contacts) + 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts.append(Contact("", "", "", ""))
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
