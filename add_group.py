# -*- coding: utf-8 -*-
from selenium import webdriver
from classes import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_new_group(Group("Test","Add new group","with parameters"))
    app.logout()
    app.assertTrue(success)

def test_add_empty_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="",header="",footer=""))
    app.logout()
    app.assertTrue(success)
