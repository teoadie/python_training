__author__ = 'Teo'
from model.group_data import Group


def test_update_first_group(app):
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
    # Count groups
    new_groups = app.group.get_all_groups()
    assert len(old_groups) == len(new_groups)
    # Check groups list
    old_groups[0] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_middle_group(app):
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
    # Count groups
    new_groups = app.group.get_all_groups()
    assert len(old_groups) == len(new_groups)
    # Check groups list
    old_groups[1] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_last_group(app):
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
    # Count groups
    new_groups = app.group.get_all_groups()
    assert len(old_groups) == len(new_groups)
    # Check groups list
    old_groups[2] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_clear_group_data(app):
    app.group.prepare_group_test_suite()
    # Create groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    old_groups = app.group.get_all_groups()
    # Update group
    changed_group = Group(name='', header='', footer='')
    changed_group.id = old_groups[0].id
    app.group.update_selected_groups([1], None)
    # Count groups
    new_groups = app.group.get_all_groups()
    assert len(old_groups) == len(new_groups)
    # Check groups list
    old_groups[0] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_several_groups(app):
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
    # Count groups
    new_groups = app.group.get_all_groups()
    assert len(old_groups) == len(new_groups)
    # Check groups list
    old_groups[1] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_update_one_group(app):
    if app.group.count() == 0:
        first_group = Group(name='First', header='FG', footer='Group1')
        app.group.create(first_group)
    old_groups = app.group.get_all_groups()
    app.group.update_selected_groups([1], None)
    # Count groups
    new_groups = app.group.get_all_groups()
    assert len(old_groups) == len(new_groups)
    # Check groups list
    changed_group = Group(name='', header='', footer='')
    changed_group.id = old_groups[0].id
    old_groups[0] = changed_group
    app.group.check_if_groups_are_equal(old_groups, new_groups)
