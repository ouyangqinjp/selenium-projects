import unittest
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
import page
import os

       
class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.cbc.ca/")
        self.driver.maximize_window()
        self.results_file = open("results.txt", "w")
        self.radio_results_file = open("radio_results.txt", "w")
        
    def first_page(self):
        self.main_page = page.MainPage(self.driver)

        """ Title """
        target = "Checking page title"
        expected = \
            "CBC.ca - Canadian News Sports Entertainment Kids Docs Radio TV"
        self.main_page.checkEqual(target, expected, self.driver.title)

        """ TAB Click and check titles for every page """
        for link_category in range(2, 4):
            if link_category == 1:
                category = "No sub_link"
                div_index = 1
                ul_index = 1
                tag_name = "a"
                expected = \
                    [ \
                    "CBC Television", \
                    "Radio Home |  CBC.ca Radio", \
                    "CBC News - Latest Canada, World, Entertainment an Business \
                    News", \
                    "CBC Sports - Sporting news, opinion, scores, standings,\
                    schedules", \
                    "CBC Music", \
                    "CBC Arts" \
                    ]

                self.main_page.click_each_link \
                    (div_index, ul_index, tag_name, expected)
#                self.title_file.write("\n")

            elif link_category == 2:
                div_index = 1
                ul_index = 2 
                tag_name = "a"
                expected = \
                    [ \
                    "Shows - CBC Player", \
                    "Radio - CBC Player", \
                    "33333333333" \
                    ]

                self.main_page.click_each_link \
                    (div_index, ul_index, tag_name, expected)
#                self.title_file.write("\n")

            elif link_category == 3:
                expected_list = []
                flag = os.path.exists("./title.txt")
                if flag:
                    f = open("title.txt")
                    for each_line in f:
                        expected_list.append("%s, " % each_line.rstrip()) 
                    f.close()
                else:
                    print "./title.txt file doesn't exist" 
                    break

                for div_index in [2, 3]:
                    ul_index = 1 
                    tag_name = "a"

                    self.main_page.click_each_link \
                        (div_index, ul_index, tag_name, expected_list)
#                    self.title_file.write("\n")

            link_category = link_category + 1
           
        self.search_results_page = page.SearchResultsPage(self.driver)

    def search(self):
        """ Search """
        for i in range(0, 3):
            if i == 0:
                page_name = self.main_page
                key_word = "shaunminions"
                #result_word = "No pages were found containing" 
                result_word = "aaaa pages were found containing" 
                flag = 0
            elif i == 1:
                page_name = self.search_results_page 
                key_word = "shaun"
                result_word = key_word
                flag = 1 
            else:
                page_name = self.search_results_page
                key_word = "minions"
                result_word = key_word
                flag = 1 

            page_name.search_text_element = key_word
            page_name.click_go_button()
            self.driver.implicitly_wait(5)
        
            """ Search Results Pagenation """
            self.search_results_page.iframe_switch() 
            self.driver.implicitly_wait(5)

            """ Search Results """
            self.search_results_page.is_results_found(result_word)

            """ get contents and write to a file """
            if flag == 1:
                for i in range(1, 3):
                    self.search_results_page.click_next()
                    self.driver.implicitly_wait(5)
                    self.search_results_page.print_search_results(key_word, i, self.results_file)
                    time.sleep(2)   
                self.results_file.write("\n")

    def radio(self):
        self.main_page = page.MainPage(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#        self.main_page.list_all_table(self.radio_results_file, 2)

        for rabel in range(3, 4):
            self.main_page.select_radio("Radio %s" % rabel)
            self.main_page.click_select_go_button()
            self.driver.implicitly_wait(5)
            self.main_page.get_table_content(self.radio_results_file, rabel)
            rabel += 1

    def login(self):
        self.main_page = page.MainPage(self.driver)

        self.main_page.get_content()
        self.main_page.click_LOGIN_button()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.main_page.click_FB_button()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print self.driver.title
        self.driver.switch_to_window(self.driver.window_handles[-2])
        self.driver.switch_to_window(self.driver.window_handles[-3])


    def test_search_in_python_org(self):
#        self.radio()
#        self.first_page()
#        self.search()
        self.login()


    def tearDown(self):
        self.results_file.close()
        self.radio_results_file.close()
#        self.title_file.close()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

