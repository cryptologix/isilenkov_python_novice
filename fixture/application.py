# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import sessionHelper

class Application:

    def  __init__(self):
        self.wd = webdriver.Chrome("C:/python27/chromedriver.exe")
        self.wd.implicitly_wait(60)
        self.session = sessionHelper(self)


    #возвращение на страницу группы
    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    #создание новой группы
    def create_new_group(self, Group):
        wd = self.wd
        self.return_to_group_page()
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


    #открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

