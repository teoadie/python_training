__author__ = 'Teo'
from model.group_data import Group


def test_add_group(app):
    app.group.prepare_group_test_suite()
    old_groups = app.group.get_all_groups()
    group = Group(name='Best friends', header='My best friends', footer='Hell yeah')
    app.group.create(group)
    # Count groups
    assert len(old_groups) + 1 == app.group.count()
    # Check groups list
    new_groups = app.group.get_all_groups()
    old_groups.append(group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_add_group_with_spaces(app):
    app.group.prepare_group_test_suite()
    old_groups = app.group.get_all_groups()
    group = Group(name=" ", header=" ", footer=" ")
    app.group.create(group)
    # Count groups
    assert len(old_groups) + 1 == app.group.count()
    # Check groups list
    new_groups = app.group.get_all_groups()
    group_on_group_page_view = Group("", "", "")
    old_groups.append(group_on_group_page_view)
    app.group.check_if_groups_are_equal(old_groups, new_groups)


def test_add_empty_group(app):
    app.group.prepare_group_test_suite()
    old_groups = app.group.get_all_groups()
    group = Group("", "", "")
    app.group.create(None)
    # Count groups
    assert len(old_groups) + 1 == app.group.count()
    # Check groups list
    new_groups = app.group.get_all_groups()
    old_groups.append(group)
    app.group.check_if_groups_are_equal(old_groups, new_groups)
