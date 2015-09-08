# -*- coding: utf-8 -*-


def test_add_contact(app, json_contacts):
    contact = json_contacts
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
