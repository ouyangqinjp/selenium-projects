from element import BasePageElement
from element import SearchPageElement
from locators import MainPageLocators
from locators import SearchResultsPageLocators 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTextElement(BasePageElement):

    locator = 'q'

class SearchTagNameElement(SearchPageElement):

    locator = 'a'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()
    search_a_element = SearchTagNameElement()


    def checkEqual(self, target, L1, L2):
        if (len(L1) == len(L2) and sorted(L1) == sorted(L2)):
            print "OK ===> expected=%s title=%s" % (L1, L2)
        else:
            print "NG ===> expected=%s title=%s" % (L1, L2)
#            print "===> len1=%s len2=%s" % (len(L1), len(L2))

    def list_all_links(self, div_index, ul_index, tag_name):
        li_lists = []
        ul_eles = self.driver \
                .find_element(By.XPATH, \
                        '//nav[@id=\'cbc-globalnav\']/div[%s]/ul[%s]' \
                        % (div_index, ul_index))
        for a_ele in ul_eles.find_elements(By.TAG_NAME, 'li'):
            li_lists.append(a_ele.text)
            ele_content = ul_eles.find_elements(By.TAG_NAME, '%s' % tag_name)
        return li_lists, ele_content, len(ele_content)

    def click_each_link(self, div_index, ul_index, tag_name, expected):
        if div_index == 2:
            self.click_LOCAL_button()
        elif div_index == 3:
            self.click_MORE_button()

        (link_text, link_eles, link_number) = \
            self.list_all_links(div_index, ul_index, tag_name)
        for i in range(0, link_number):
            (link_text, link_eles, link_number) = \
                self.list_all_links(div_index, ul_index, tag_name)
            link_eles[i].click()
            self.driver.implicitly_wait(10)

#            title_file.write("Page=%s: \t %s \n" % (i, self.driver.title))
            target = "click_each_link: link_number=%s i=%s Checking page title --%s" \
                     % (link_number, i, self.driver.title)

            self.checkEqual(target, expected[i], self.driver.title)
            self.go_back()
            self.driver.implicitly_wait(5)
            if div_index == 2:
                self.click_LOCAL_button()
            elif div_index == 3:
                self.click_MORE_button()

            i = i + 1

    def click_LOCAL_button(self):
        element = self.driver.find_element(*MainPageLocators.LOCAL_BUTTON)
        element.click()

    def click_MORE_button(self):
        element = self.driver.find_element(*MainPageLocators.MORE_BUTTON)
        element.click()

    def click_LOGIN_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_FB_button(self):
        element = self.driver.find_element(*MainPageLocators.FB_BUTTON)
        element.click()

    def select_radio(self, labels):
        element = self.driver.find_element(*MainPageLocators.SELECT_BUTTON)
        for option in element.find_elements_by_tag_name('option'):
            if option.text == labels:
                option.click()
                break

    def click_select_go_button(self):
        element = self.driver.find_element(*MainPageLocators.SELECT_GO_BUTTON)
        element.click()

    def click_select_listen_button(self):
        element = self.driver.find_element(*MainPageLocators.SELECT_LISTEN_BUTTON)
        element.click()


    def list_all_table(self, result_file, radio_rabel):
        print "radio_rabel= %s" % radio_rabel
        table = self.driver.find_element(*MainPageLocators.TABLE)
        for tr in table.find_elements_by_tag_name('tr'):
            if len(tr.text) != 0:
                tr_tmp = tr.text.split("\n")
                result_file.write("Radio_%s  %s : %s \n" \
                    % (radio_rabel, tr_tmp[0], tr_tmp[-1]))
#                tds = tr.find_elements(By.TAG_NAME, 'td')
                td_a = table.find_elements(By.TAG_NAME, 'a')
        return td_a, len(td_a)

    def get_table_content(self, result_file, radio_rabel):
        (td_a, td_a_len) = self.list_all_table(result_file, radio_rabel)
        for i in range(0, td_a_len) :
        #for i in range(0, 1) :
            try:
                (td_a, td_a_len) = self.list_all_table(result_file, radio_rabel)
                print "get_table_content, i=%s" % i
                print "get_table_content, i=%s, td_a=%s" % (i, td_a[i])
                if len(td_a[i].text) != 0:
                    td_a[i].click()
                    self.driver.implicitly_wait(5)
                    self.go_back()
            except Exception as e:
                print "type:" + str(type(e))
                print "args:" + str(e.args)
                print "message:" + e.message
                print "contents:" + str(e)
            print "Try and assert finished"

    def list_all_content(self):
        div_eles = self.driver.find_element(*MainPageLocators.CONTENTS)
        for div in div_eles.find_elements(By.TAG_NAME, 'div'):
            div_a = div_eles.find_elements(By.TAG_NAME, 'a')
        return div_a, len(div_a)

    def get_content(self):
        (a_eles, len_a) = self.list_all_content() 
        for i in range(0, len_a):
            (a_eles, len_a) = self.list_all_content() 
            print "%s %s" % (i, a_eles[i].text)
            a_eles[i].click()
            self.driver.implicitly_wait(5)
            self.go_back()







#                print "TR=%s \t TD=%s" % (tr.text, td.text) 
#                result_file.write("%s \n" % td.text)

    def click_tv_go_button(self):
        element = self.driver.find_element(*MainPageLocators.TV_GO_BUTTON)
        element.click()

    def go_back(self):
        self.driver.back()
 

class SearchResultsPage(BasePage):

    search_text_element = SearchTextElement()

    def is_results_found(self, pageText):
        print "Trying to assert === >> %s " % pageText
        try:
            assert pageText in self.driver.page_source
            print "Try End"
        except Exception as e:
            print "Error!"
            print "type:" + str(type(e))
            print "args:" + str(e.args)
            print "message:" + e.message
            print "contents:" + str(e)
        print "Try and assert finished"


   
    def iframe_switch(self):
        iframe = self.driver.find_element(*SearchResultsPageLocators.IFRAME)
        print "Switch to iframe...   Done"
        return self.driver.switch_to_frame(iframe)

    def click_next(self):
        table = self.driver.find_element(*SearchResultsPageLocators.TABLE)

        for tr in table.find_elements(By.TAG_NAME, 'tr'):
            tds = tr.find_elements(By.TAG_NAME, 'td')
            next_element = tds[-1] \
                .find_element(By.CLASS_NAME, 'b') \
                .find_element(By.TAG_NAME, 'a')
            next_element.click()

    def print_search_results(self, keyword, i, result_file):
        p_eles = self.driver.find_elements(By.CLASS_NAME, 'g')
        for p_ele in p_eles:
            a_ele = p_ele.find_element(By.TAG_NAME, 'a') \
                     .find_element(By.TAG_NAME, 'span')
            result_file.write("%s Page=%s: \t %s \n" % (keyword, i, a_ele.text))

    def click_go_button(self):
        element = self.driver.find_element(*SearchResultsPageLocators.GO_BUTTON)
        element.click()


