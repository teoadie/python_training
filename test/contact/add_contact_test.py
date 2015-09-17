# -*- coding: utf-8 -*-


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    app.contact.prepare_contact_test_suite()
    old_contacts = db.get_contact_list()
    # Create new contact
    app.contact.create(contact)
    # Check contacts list
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
    if check_ui:
        new_contacts = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(old_contacts, new_contacts)
