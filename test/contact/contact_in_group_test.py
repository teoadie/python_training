__author__ = 'Teo'
import random
from model.group_data import Group
from model.contact_data import Contact


def test_add_one_contact_to_group(app, db, check_ui):
    # Prepare groups
    app.group.prepare_group_test_suite()
    new_group = Group(name="Group to add", footer="Some footer", header="Some header")
    app.group.create(new_group)
    groups = db.get_group_list()
    new_group.id = groups[0].id
    # Prepare contacts
    app.contact.prepare_contact_test_suite()
    app.contact.create(Contact(firstname="Contact1", lastname="Di"))
    contact = db.get_contact_list()[0]
    # Add contact to group
    app.contact.add_contacts_by_ids_to_group([contact.id], new_group.name)
    # Check contacts and group links
    contacts_in_group = db.get_contacts_in_group(new_group)
    expected_contacts_in_group = [contact]
    app.contact.check_if_contacts_are_equal(expected_contacts_in_group, contacts_in_group)
    if check_ui:
        # Change group view
        app.contact.set_group_view_on_contact_page(new_group.name)
        # Check contact list
        contacts_in_group_by_ui = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(contacts_in_group_by_ui, expected_contacts_in_group)


def test_add_several_contacts_to_group(app, db, check_ui):
    # Prepare groups
    app.group.prepare_group_test_suite()
    new_group = Group(name="Group to add", footer="Some footer", header="Some header")
    app.group.create(new_group)
    groups = db.get_group_list()
    new_group.id = groups[0].id
    # Prepare contacts
    app.contact.prepare_contact_test_suite()
    app.contact.create(Contact(firstname="Contact1", lastname="Di"))
    app.contact.create(Contact(firstname="Contact2", lastname="Do"))
    app.contact.create(Contact(firstname="Contact3", lastname="Da"))
    contacts = db.get_contact_list()
    first_contact = db.get_contact_list()[0]
    second_contact = db.get_contact_list()[1]
    # Add contact to group
    app.contact.add_contacts_by_ids_to_group([first_contact.id, second_contact.id], new_group.name)
    # Check contacts and group links
    contacts_in_group = db.get_contacts_in_group(new_group)
    expected_contacts_in_group = [first_contact, second_contact]
    app.contact.check_if_contacts_are_equal(expected_contacts_in_group, contacts_in_group)
    if check_ui:
        # Change group view
        app.contact.set_group_view_on_contact_page(new_group.name)
        # Check contact list
        contacts_in_group_by_ui = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(contacts_in_group_by_ui, expected_contacts_in_group)


def test_delete_all_contacts_from_group(app, db, check_ui):
    # Prepare groups
    app.group.prepare_group_test_suite()
    new_group = Group(name="Group to add", footer="Some footer", header="Some header")
    app.group.create(new_group)
    groups = db.get_group_list()
    new_group.id = groups[0].id
    # Prepare contacts
    app.contact.prepare_contact_test_suite()
    app.contact.create(Contact(firstname="Contact1", lastname="Di"))
    app.contact.create(Contact(firstname="Contact2", lastname="Do"))
    contact = db.get_contact_list()[0]
    # Add contact to group
    app.contact.add_contacts_by_ids_to_group([contact.id], new_group.name)
    # Remove contact from group
    app.contact.set_group_view_on_contact_page(new_group.name)
    app.contact.remove_contacts_by_ids_from_group([contact.id])
    # Check contacts in group
    assert 0 == len(db.get_contacts_in_group(new_group))
    # Check contacts outside group
    contacts_outside_group = db.get_contacts_not_in_group(new_group)
    all_contacts = db.get_contact_list()
    app.contact.check_if_contacts_are_equal(all_contacts, contacts_outside_group)
    if check_ui:
        # Change group view
        app.contact.set_group_view_on_contact_page(new_group.name)
        # Check contact list
        assert 0 == app.contact.count()


def test_delete_several_contacts_from_group(app, db, check_ui):
    # Prepare groups
    app.group.prepare_group_test_suite()
    new_group = Group(name="Group to add", footer="Some footer", header="Some header")
    app.group.create(new_group)
    groups = db.get_group_list()
    new_group.id = groups[0].id
    # Prepare contacts
    app.contact.prepare_contact_test_suite()
    app.contact.create(Contact(firstname="Contact1", lastname="Di"))
    app.contact.create(Contact(firstname="Contact2", lastname="Do"))
    app.contact.create(Contact(firstname="Contact3", lastname="Da"))
    first_contact = db.get_contact_list()[0]
    second_contact = db.get_contact_list()[1]
    third_contact = db.get_contact_list()[2]
    # Add contact to group
    app.contact.add_contacts_by_ids_to_group([first_contact.id, second_contact.id, third_contact.id], new_group.name)
    # Remove contact from group
    app.contact.set_group_view_on_contact_page(new_group.name)
    app.contact.remove_contacts_by_ids_from_group([first_contact.id, third_contact.id])
    # Check contacts in group
    contacts_in_group = db.get_contacts_in_group(new_group)
    expected_contacts_in_group = [second_contact]
    app.contact.check_if_contacts_are_equal(expected_contacts_in_group, contacts_in_group)
    # Check contacts outside group
    contacts_outside_group = db.get_contacts_not_in_group(new_group)
    expected_contacts_outside_group = db.get_contact_list()
    expected_contacts_outside_group.remove(second_contact)
    app.contact.check_if_contacts_are_equal(expected_contacts_outside_group, contacts_outside_group)
    if check_ui:
        # Check contacts in group
        app.contact.set_group_view_on_contact_page(new_group.name)
        contacts_in_group_by_ui = app.contact.get_all_contacts()
        app.contact.check_if_contacts_are_equal(expected_contacts_in_group, contacts_in_group_by_ui)
