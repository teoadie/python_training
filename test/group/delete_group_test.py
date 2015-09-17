__author__ = 'Teo'
from model.group_data import Group
import random


def test_delete_the_only_one_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    app.group.create(None)
    app.group.delete_selected_groups([1])
    # Check existing groups
    assert 0 == len(db.get_group_list())
    if check_ui:
        assert 0 == len(app.group.count_groups())


def test_delete_first_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create two groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    old_groups = db.get_group_list()
    # Delete first
    app.group.delete_selected_groups([1])
    # Check existing groups
    new_groups = db.get_group_list()
    old_groups[0:1] = []
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_delete_middle_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create three groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    old_groups = db.get_group_list()
    # Delete group
    app.group.delete_selected_groups([2])
    # Check existing groups
    new_groups = db.get_group_list()
    old_groups[1:2] = []
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_delete_last_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create three groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    old_groups = db.get_group_list()
    # Delete group
    app.group.delete_selected_groups([3])
    # Check existing groups
    new_groups = db.get_group_list()
    old_groups[2:3] = []
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_delete_all_groups(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create three groups
    app.group.create(None)
    app.group.create(None)
    app.group.create(None)
    # Select all groups and delete them
    app.group.delete_all_groups()
    assert 0 == len(db.get_group_list())
    if check_ui:
        assert 0 == app.group.count()


def test_delete_several_selected_groups(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create four groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    fourth_group = Group(name='WWW', header='W', footer='Group4')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    app.group.create(fourth_group)
    # Select two groups to delete
    old_groups = db.get_group_list()
    first_deleted_group = old_groups[1]
    second_deleted_group = old_groups[3]
    # Select two groups and delete them
    app.group.delete_groups_by_ids([first_deleted_group.id, second_deleted_group.id])
    # Check existing groups
    old_groups.remove(first_deleted_group)
    old_groups.remove(second_deleted_group)
    new_groups = db.get_group_list()
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_delete_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(None)
    old_groups = db.get_group_list()
    # Create random index
    group = random.choice(old_groups)
    app.group.delete_groups_by_ids([group.id])
    new_groups = db.get_group_list()
    old_groups.remove(group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)
