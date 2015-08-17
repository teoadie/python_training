# -*- coding: utf-8 -*-
from model.contact_data import Contact


def test_add_contact(app):
    # Create new contact object and fill its data
    contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    contact.set_company_data(title="MegaMailGroutOfAllWorld", company="MegaMailGroupOfAllWorldCorporation",
                             address="somewhere beyond the sea")
    contact.set_emails(first="ann.arner@megamailgroupofallworldcorporation.com",
                       second="ann@annhomemail.org", third="annnew@annhomemail.org")
    contact.set_homepage("www.somewherebeyondthesea.com")
    contact.set_phones(home="112223366", mobile="+7(000)9999911111222", work="44444433", fax="2300011")
    contact.set_second_info(address="World 36", home="77", notes="She is my friend")
    contact.set_birthday(day="4", month="4", year="1987")
    contact.set_anniversary(day="31", month="7", year="2010")
    # Create new contact
    app.contact.prepare_contact_test_suite()
    app.contact.create(contact)


def test_add_empty_contact(app):
    # Create new contact
    app.contact.prepare_contact_test_suite()
    app.contact.create(None)


def test_add_contact_with_spaces_in_fields(app):
    # Create new contact object and fill its data
    contact = Contact(firstname=" ", middlename=" ", lastname=" ", nickname=" ")
    contact.set_company_data(title=" ", company=" ", address=" ")
    contact.set_emails(first=" ", second=" ", third=" ")
    contact.set_homepage(" ")
    contact.set_phones(home=" ", mobile=" ", work=" ", fax=" ")
    contact.set_second_info(address=" ", home=" ", notes=" ")
    contact.set_birthday(day="1", month="1", year=" ")
    contact.set_anniversary(day="1", month="1", year=" ")
    # Create new contact
    app.contact.prepare_contact_test_suite()
    app.contact.create(contact)


def test_add_several_contacts(app):
    # Create new contact object and fill its data
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    # Create new contact
    app.contact.prepare_contact_test_suite()
    app.contact.create(first_contact)
    app.contact.create(second_contact)
