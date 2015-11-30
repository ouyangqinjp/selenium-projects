import unittest
import time
#from datetime import datetime, date, time
from selenium.webdriver.common.by import By

from selenium import webdriver
import page
import os
import sys

       
class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://adam.goucher.ca/parkcalc/")
#        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
#        self.results_file = open("results.txt", "w")
#        self.radio_results_file = open("radio_results.txt", "w")
        
    def first_page(self):
        self.main_page = page.MainPage(self.driver)

#        self.main_page.list_all_options()
        entry_time_list = ["02:00", "12:00", "13:50", "20:59"]
        entry_month_list = ["June", "Auguest", "May", "December"]
        entry_date_list = ["2", "5", "10", "30"]

        leave_time_list = ["00:03", "12:00", "13:50", "23:59"]
        leave_month_list = ["June", "September", "July", "December"]
        leave_date_list = ["3", "8", "15", "30"]

        i = 0
        for i in range(len(entry_month_list)):
            entry_month = entry_month_list[i]
            entry_date = entry_date_list[i]
            entry_time = entry_time_list[i]
            leave_month = leave_month_list[i]
            leave_date = leave_date_list[i]
            leave_time = leave_time_list[i]
            print "entry i=%s %s %s -- %s " \
                % (i, entry_month, entry_date, entry_time)

            print "leave i=%s %s %s -- %s " \
                % (i, leave_month, leave_date, leave_time)

            """ Entry Date """
            self.main_page.input_entry_date = entry_time
            self.main_page.click_radio_PM()
            self.main_page.click_calender_img("EntryDate")
            self.driver.switch_to_window(self.driver.window_handles[-1])
            self.main_page.click_calender_date(entry_month, entry_date)
            time.sleep(5)

            """ Leave Date """
            self.main_page.input_exist_date = leave_time
            self.main_page.click_calender_img("LeaveDate")
            self.driver.switch_to_window(self.driver.window_handles[-1])
            self.main_page.click_calender_date(leave_month, leave_date)
            time.sleep(5)

    #        print self.driver.find_element(By.NAME, 'EntryDate').text

    def test_search_in_python_org(self):
        self.first_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

