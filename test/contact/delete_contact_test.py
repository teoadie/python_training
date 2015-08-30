__author__ = 'Teo'
from model.contact_data import Contact
from random import randrange


def test_delete_the_only_one_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    app.contact.create(first_contact)
    old_contacts = app.contact.get_all_contacts()
    # Delete contact
    app.contact.delete_selected_contacts([1])
    # Count contacts
    assert len(old_contacts) - 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts[0:1] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_first_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    old_contacts = app.contact.get_all_contacts()
    # Delete contact
    app.contact.delete_selected_contacts([1])
    # Count contacts
    assert len(old_contacts) - 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts[0:1] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_middle_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    old_contacts = app.contact.get_all_contacts()
    # Delete contact
    app.contact.delete_selected_contacts([2])
    # Count contacts
    assert len(old_contacts) - 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts[1:2] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_last_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    old_contacts = app.contact.get_all_contacts()
    # Delete contact
    app.contact.delete_selected_contacts([3])
    # Count contacts
    assert len(old_contacts) - 1 == app.contact.count()
    # Check contacts list
    new_contacts = app.contact.get_all_contacts()
    old_contacts[2:3] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_all_contacts(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.delete_all_contacts()
    # Count contacts
    assert 0 == app.contact.count()


def test_delete_contact_from_update_page(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    app.contact.create(first_contact)
    old_contacts = app.contact.get_all_contacts()
    app.contact.delete_contact_from_update_page(1)
    # Count contacts
    assert len(old_contacts) - 1 == app.contact.count()
    # Check contacts list
    old_contacts[0:1] = []
    new_contacts = app.contact.get_all_contacts()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_several_selected_contacts(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    fourth_contact = Contact(firstname="Rich", middlename="Rich", lastname="Rock", nickname="Lin")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.create(fourth_contact)
    old_contacts = app.contact.get_all_contacts()
    # Delete contacts
    app.contact.delete_selected_contacts([1, 3])
    # Count contacts
    assert len(old_contacts) - 2 == app.contact.count()
    # Check contacts list
    old_contacts[0:1] = []
    old_contacts[1:2] = []
    new_contacts = app.contact.get_all_contacts()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(None)
    old_contacts = app.contact.get_all_contacts()
    index = randrange(len(old_contacts))
    # Delete contacts
    app.contact.delete_selected_contacts([index + 1])
    # Count contacts
    assert len(old_contacts) - 1 == app.contact.count()
    # Check contacts list
    old_contacts[index:index + 1] = []
    new_contacts = app.contact.get_all_contacts()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
