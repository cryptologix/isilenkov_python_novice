# -*- coding: utf-8 -*-
class groupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, Group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        self.fill_group_form(Group)
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, Group):
        wd = self.app.wd
        self.change_field_value("group_name", Group.name)
        self.change_field_value("group_header", Group.header)
        self.change_field_value("group_footer", Group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.open_group_page()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #open modify form
        wd.find_element_by_name("edit").click()
        #fill form
        self.fill_group_form(new_group_data)
        #submit modify
        wd.find_element_by_name("update").click()
        self.open_group_page()

