# -*- coding: utf-8 -*-
import pytest
from fixtures.group_fixture import GroupFixture
from model.group_data import Group


@pytest.fixture
def app(request):
    fixture = GroupFixture()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login()
    group = Group(name='Best friends', header='My best friends', footer='Hell yeah')
    app.open_group_page_and_create_new_group(group)
    app.logout()


def test_add_group_with_spaces(app):
    app.login()
    group = Group(name=' ', header=' ', footer=' ')
    app.open_group_page_and_create_new_group(group)
    app.logout()


def test_add_empty_group(app):
    app.login()
    app.open_group_page_and_create_new_group(None)
    app.logout()
