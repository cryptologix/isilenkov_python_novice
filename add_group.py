# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from classes import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome("C:/python27/chromedriver.exe")
        #self.wd = webdriver.Chrome("C:/chromedriver.exe")
        self.wd.implicitly_wait(60)


    def test_add_group(self):
        success = True

        wd = self.wd

        self.login(wd, "admin", "secret")
        self.create_new_group(wd,Group("Test","Add new group","with parameters"))
        self.return_to_group_page(wd)
        self.logout(wd)

        self.assertTrue(success)


    def test_add_empty_group(self):
        success = True

        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_group(wd,Group(name="",header="",footer=""))
        self.logout(wd)

        self.assertTrue(success)


    def logout(self, wd):
        self.return_to_group_page(wd)
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, wd, Group):
        self.return_to_group_page(wd)
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        wd.find_element_by_name("submit").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
