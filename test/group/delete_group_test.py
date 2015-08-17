__author__ = 'Teo'
from model.group_data import Group


def test_delete_the_only_one_group(app):
    app.group.prepare_group_test_suite()
    app.group.create(None)
    app.group.delete_selected_groups([1])


def test_delete_first_group(app):
    app.group.prepare_group_test_suite()
    # Create two groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    # Delete first
    app.group.delete_selected_groups([1])


def test_delete_middle_group(app):
    app.group.prepare_group_test_suite()
    # Create three groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    # Delete group
    app.group.delete_selected_groups([2])


def test_delete_last_group(app):
    app.group.prepare_group_test_suite()
    # Create three groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    # Delete group
    app.group.delete_selected_groups([3])


def test_delete_all_selected_groups(app):
    app.group.prepare_group_test_suite()
    # Create three groups
    app.group.create(None)
    app.group.create(None)
    app.group.create(None)
    # Select all groups and delete them
    app.group.delete_all_groups()


def test_delete_several_selected_groups(app):
    app.group.prepare_group_test_suite()
    # Create four groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    third_group = Group(name='Third', header='TG', footer='Group3')
    fourth_group = Group(name='Four', header='TG', footer='Group4')
    app.group.create(first_group)
    app.group.create(second_group)
    app.group.create(third_group)
    app.group.create(fourth_group)
    # Select two groups and delete them
    app.group.delete_selected_groups([1, 3])
