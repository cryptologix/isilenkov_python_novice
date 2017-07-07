# -*- coding: utf-8 -*-
class sessionHelper:

    def __init__(self,app):
        self.app = app

    # выход
    def logout(self):
        wd = self.app.wd
        self.app.return_to_group_page()
        wd.find_element_by_link_text("Logout").click()

     # вход
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
