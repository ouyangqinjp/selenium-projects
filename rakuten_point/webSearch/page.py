import time
#from datetime import datetime, date, time
from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class InputText(BasePageElement):

    def __init__(self, flag, name):
        self.locator = name
        self.flag = flag 

class MainPage(BasePage):

    string_username = ('ByName', 'u')
    username = InputText(*string_username)

    string_password = ('ByName', 'p')
    password = InputText(*string_password)

    search_keyword = ('ByName', 'qt')
    keyword = InputText(*search_keyword)

    def click_login(self):
        locator = MainPageLocators.LOGIN_BUTTON
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 300).until(lambda driver: element)
        element.click()

    def click_submit(self):
        locator = MainPageLocators.SUBMIT_BUTTON
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 300).until(lambda driver: element)
        element.click()

    def click_search(self):
        locator = MainPageLocators.SEARCH_BUTTON
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 300).until(lambda driver: element)
        element.click()




    def click_link(self):
        locator = MainPageLocators.POINT_LINK
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 300).until(lambda driver: element)
        element.click()

    def list_all_div(self):
        span_locator = MainPageLocators.SPAN_ID
        span = self.driver.find_element(*span_locator)
        WebDriverWait(self.driver, 300).until(lambda driver: span)
        #div_list = span.find_elements(By.ID, '*\'position\']')
        div_list = span.find_elements(By.XPATH, \
                '//div[starts-with(@id,\'position\')]')
        print "len div_list %s" % len(div_list)
        return div_list

    def click_banner(self):

        div_list = self.list_all_div()
        ori_window = self.driver.window_handles
        print "ori_window %s " % ori_window

        i = 0
        #for each_div in div_list:
        for i in range(len(div_list)):
            div_list = self.list_all_div()
            self.driver.implicitly_wait(10)

            print "i=%s len=%s %s" % (i, len(div_list), div_list[i].get_attribute("id"))
            a_ele = div_list[i].find_element(By.XPATH, 'div[2]/div[1]/a/img')
            print "i=%s a_element %s" % (i, a_ele.get_attribute("alt"))
            a_ele.click()

            print "1 current window_handles %s" % self.driver.current_window_handle
            self.driver.switch_to_window(self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to_window(ori_window)
            print "2 current window_handles %s" % self.driver.current_window_handle
            i += 1

    def click_radio_PM(self):
        locator = MainPageLocators.RADIO_ID
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 300).until(lambda driver: element)
        element.click()

    def click_calender_img(self, img_locator):
        print "img %s" % img_locator
        #locator = MainPageLocators.CAL_IMG
        if img_locator == "EntryDate":
            locator = MainPageLocators.IMG_ENTRY
        #elif img_locator == "LeaveTime":
        elif img_locator == "LeaveDate":
            locator = MainPageLocators.IMG_LEAVE

        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 300).until(lambda driver: element)
        element.click()

    def click_calender_date(self, month, date):
        select = self.driver.find_element(By.NAME, 'MonthSelector')
        option_list = select.find_elements(By.TAG_NAME, 'option')
        for each_option in option_list:
            print "%s %s" % (each_option.text, month)
            if each_option.text == month:
                each_option.click()

                break
        time.sleep(3)


        tr_list = self.driver.find_elements(By.TAG_NAME, 'tr')
        for eachTr in tr_list:
            td_list = eachTr.find_elements(By.TAG_NAME, 'td')
            if len(td_list) == 7:
                a_list = eachTr.find_elements(By.TAG_NAME, 'a')
                for eachA in a_list:
                    print "a_date text = %s" % eachA.text
                    if eachA.text == date:
                        eachA.click()
                        self.driver.switch_to_window(self.driver.window_handles[-1])
                        return

 

        



