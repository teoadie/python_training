__author__ = 'Teo'
from model.group_data import Group
import random


def test_update_first_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    old_groups = app.group.get_all_groups()
    # Update group
    changed_group = Group(name='New', header='NG', footer='Better group')
    changed_group.id = old_groups[0].id
    app.group.update_selected_groups([1], changed_group)
    # Check groups list
    new_groups = db.get_group_list()
    old_groups[0] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_middle_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    old_groups = app.group.get_all_groups()
    # Update group
    changed_group = Group(name='New', header='NG', footer='Better group')
    changed_group.id = old_groups[1].id
    app.group.update_selected_groups([2], changed_group)
    # Check groups list
    new_groups = db.get_group_list()
    old_groups[1] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_last_group(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    old_groups = app.group.get_all_groups()
    # Update group
    changed_group = Group(name='New', header='NG', footer='Better group')
    changed_group.id = old_groups[2].id
    app.group.update_selected_groups([3], changed_group)
    # Check groups list
    new_groups = db.get_group_list()
    old_groups[2] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_clear_group_data(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    old_groups = db.get_group_list()
    # Update group
    changed_group = Group(name='', header='', footer='')
    group_id = old_groups[0].id
    changed_group.id = group_id
    app.group.update_groups_by_ids([group_id], None)
    # Check groups list
    new_groups = db.get_group_list()
    old_groups[0] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_several_groups(app, db, check_ui):
    app.group.prepare_group_test_suite()
    # Create groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    fourth_group = Group(name='Fourth', header='FG', footer='Group4')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    app.group.create(fourth_group)
    old_groups = app.group.get_all_groups()
    # Update group
    changed_group = Group(name='New', header='NG', footer='Better group')
    changed_group.id = old_groups[1].id
    app.group.update_selected_groups([2, 4], changed_group)
    # Check groups list
    new_groups = db.get_group_list()
    old_groups[1] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        first_group = Group(name='First', header='FG', footer='Group1')
        app.group.create(first_group)
    old_groups = db.get_group_list()
    # Create random group
    group = random.choice(old_groups)
    app.group.update_groups_by_ids([group.id], None)
    # Check groups list
    new_groups = db.get_group_list()
    changed_group = Group(name='', header='', footer='')
    changed_group.id = group.id
    old_groups.remove(group)
    old_groups.append(changed_group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)
    if check_ui:
        new_groups = app.group.get_all_groups()
        app.group.check_if_groups_are_equal(old_groups, new_groups)
