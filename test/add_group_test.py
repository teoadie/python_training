# -*- coding: utf-8 -*-
from model.group_data import Group


def test_add_group(app):
    app.session.login_as_admin()
    group = Group(name='Best friends', header='My best friends', footer='Hell yeah')
    app.group.create(group)
    app.session.logout()


def test_add_group_with_spaces(app):
    app.session.login_as_admin()
    group = Group(name=' ', header=' ', footer=' ')
    app.group.create(group)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login_as_admin()
    app.group.create(None)
    app.session.logout()
