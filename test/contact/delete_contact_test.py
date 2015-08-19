__author__ = 'Teo'
from model.contact_data import Contact


def test_delete_the_only_one_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    app.contact.create(first_contact)
    app.contact.delete_selected_contacts([1])


def test_delete_first_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.delete_selected_contacts([1])


def test_delete_middle_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.delete_selected_contacts([2])


def test_delete_last_contact(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.delete_selected_contacts([3])


def test_delete_all_contacts(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    second_contact = Contact(firstname="Don", middlename="JD", lastname="Doe", nickname="Jay")
    third_contact = Contact(firstname="Leo", middlename="LLL", lastname="Lemon", nickname="Lem")
    app.contact.create(first_contact)
    app.contact.create(second_contact)
    app.contact.create(third_contact)
    app.contact.delete_all_contacts()


def test_delete_one_contact(app):
    if app.contact.count() == 0:
        app.contact.create(None)
    app.contact.delete_selected_contacts([1])


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
    app.contact.delete_selected_contacts([1, 3])


def test_delete_contact_from_update_page(app):
    app.contact.prepare_contact_test_suite()
    first_contact = Contact(firstname="Ann", middlename="AT", lastname="Arner", nickname="Tee")
    app.contact.create(first_contact)
    app.contact.delete_contact_from_update_page(1)
