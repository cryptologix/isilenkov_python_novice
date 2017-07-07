# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.classes import Group



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group(name="",header="",footer=""))
    app.session.logout()

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group("Test","Add new group","with parameters"))
    app.session.logout()

