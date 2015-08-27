__author__ = 'Teo'
from model.group_data import Group


def test_delete_the_only_one_group(app):
    app.group.prepare_group_test_suite()
    app.group.create(None)
    old_groups = app.group.get_all_groups()
    app.group.delete_selected_groups([1])
    new_groups = app.group.get_all_groups()
    # Count groups
    assert len(old_groups) - 1 == len(new_groups)
    # Check existing groups
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_first_group(app):
    app.group.prepare_group_test_suite()
    # Create two groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    old_groups = app.group.get_all_groups()
    # Delete first
    app.group.delete_selected_groups([1])
    new_groups = app.group.get_all_groups()
    # Count groups
    assert len(old_groups) - 1 == len(new_groups)
    # Check existing groups
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_middle_group(app):
    app.group.prepare_group_test_suite()
    # Create three groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    old_groups = app.group.get_all_groups()
    # Delete group
    app.group.delete_selected_groups([2])
    new_groups = app.group.get_all_groups()
    # Count groups
    assert len(old_groups) - 1 == len(new_groups)
    # Check existing groups
    old_groups[1:2] = []
    assert old_groups == new_groups


def test_delete_last_group(app):
    app.group.prepare_group_test_suite()
    # Create three groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    old_groups = app.group.get_all_groups()
    # Delete group
    app.group.delete_selected_groups([3])
    new_groups = app.group.get_all_groups()
    # Count groups
    assert len(old_groups) - 1 == len(new_groups)
    # Check existing groups
    old_groups[2:3] = []
    assert old_groups == new_groups


def test_delete_all_groups(app):
    app.group.prepare_group_test_suite()
    # Create three groups
    app.group.create(None)
    app.group.create(None)
    app.group.create(None)
    # Select all groups and delete them
    app.group.delete_all_groups()
    new_groups = app.group.get_all_groups()
    assert 0 == len(new_groups)


def test_delete_one_group(app):
    old_groups = app.group.get_all_groups()
    if app.group.count() == 0:
        app.group.create(None)
    app.group.delete_selected_groups([1])
    new_groups = app.group.get_all_groups()
    # Count groups
    assert len(old_groups) == len(new_groups)


def test_delete_several_selected_groups(app):
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
    old_groups = app.group.get_all_groups()
    # Select two groups and delete them
    app.group.delete_selected_groups([1, 3])
    new_groups = app.group.get_all_groups()
    # Count groups
    assert len(old_groups) - 2 == len(new_groups)
    # Check existing groups
    old_groups[0:1] = []
    old_groups[1:2] = []
    assert old_groups == new_groups
