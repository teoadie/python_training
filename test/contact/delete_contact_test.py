__author__ = 'Teo'
from model.contact_data import Contact
import random


def test_delete_the_only_one_contact(app, db, check_ui):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    app.contact.create(first_contact)
    # Delete contact
    app.contact.delete_selected_contacts([1])
    # Check contacts list
    assert 0 == len(db.get_contact_list())
    if check_ui:
        assert 0 == app.contact.count()


def test_delete_first_contact(app, db, check_ui):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    old_contacts = app.contact.get_all_contacts()
    # Delete contact
    app.contact.delete_selected_contacts([1])
    # Check contacts list
    new_contacts = db.get_contact_list()
    old_contacts[0:1] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_middle_contact(app, db, check_ui):
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
    # Check contacts list
    new_contacts = db.get_contact_list()
    old_contacts[1:2] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_last_contact(app, db, check_ui):
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
    # Check contacts list
    new_contacts = db.get_contact_list()
    old_contacts[2:3] = []
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_all_contacts(app, db, check_ui):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.delete_all_contacts()
    # Count contacts
    assert 0 == len(db.get_contact_list())
    if check_ui:
        assert 0 == app.contact.count()


def test_delete_contact_from_update_page(app, db, check_ui):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    app.contact.create(first_contact)
    app.contact.delete_contact_from_update_page(1)
    # Count contacts
    assert 0 == len(db.get_contact_list())
    if check_ui:
        assert 0 == app.contact.count()


def test_delete_several_selected_contacts(app, db, check_ui):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    fourth_contact = Contact(firstname="Rich", middlename="Rich", lastname="Rock", nickname="Lin")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.create(fourth_contact)
    # Select two contacts to delete
    old_contacts = db.get_contact_list()
    first_deleted_contact = old_contacts[1]
    second_deleted_contact = old_contacts[3]
    # Delete contacts
    app.contact.delete_contacts_by_ids([first_deleted_contact.id, second_deleted_contact.id])
    # Check contacts list
    old_contacts.remove(first_deleted_contact)
    old_contacts.remove(second_deleted_contact)
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(None)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # Delete contacts
    app.contact.delete_contacts_by_ids([contact.id])
    # Check contacts list
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
