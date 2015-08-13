__author__ = 'Teo'
from model.group_data import Group


def test_add_group(app):
    app.session.login_as_admin()
    app.group.prepare_group_test_suite()
    group = Group(name='Best friends', header='My best friends', footer='Hell yeah')
    app.group.create(group)
    app.session.logout()


def test_add_group_with_spaces(app):
    app.session.login_as_admin()
    app.group.prepare_group_test_suite()
    group = Group(name=' ', header=' ', footer=' ')
    app.group.create(group)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login_as_admin()
    app.group.prepare_group_test_suite()
    app.group.create(None)
    app.session.logout()


def test_add_several_groups(app):
    app.session.login_as_admin()
    app.group.prepare_group_test_suite()
    # Create two groups
    first_group = Group(name='First', header='FG', footer='Group1')
    second_group = Group(name='Second', header='SG', footer='Group2')
    app.group.create(first_group)
    app.group.create(second_group)
    app.session.logout()


