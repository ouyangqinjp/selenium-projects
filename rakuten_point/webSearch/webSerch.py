#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
#from datetime import datetime, date, time
from selenium.webdriver.common.by import By

from selenium import webdriver
import page
import os
import sys


class WebSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://websearch.rakuten.co.jp/")
#        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
#        self.results_file = open("results.txt", "w")
#        self.radio_results_file = open("radio_results.txt", "w")
 
    def first_page(self):
        self.main_page = page.MainPage(self.driver)

        self.main_page.click_login()
        self.main_page.username = "username"
        self.main_page.password = "password"
        self.main_page.click_submit()

        keyword_jp = "ご飯"
        self.main_page.keyword = unicode(keyword_jp, 'utf-8') 
        self.main_page.click_search()

        time.sleep(5)





    def test_search_in_python_org(self):
        self.first_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


