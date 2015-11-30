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

    string_entryTime = ('ByName', 'EntryTime')
    input_entry_date = InputText(*string_entryTime)

    #string_existTime = ('ByXpath', '//*[@id=\'ExitTime\']')
    string_existTime = ('ByName', 'ExitTime')
    input_exist_date = InputText(*string_existTime)


    def list_all_options(self):
        select_locator = MainPageLocators.SELECT_ID
        select = self.driver.find_element(*select_locator)
        WebDriverWait(self.driver, 300).until(lambda driver: select)
        option_content = select.find_elements(By.TAG_NAME, 'option')

        for option_ele in option_content:
            self.driver.implicitly_wait(300)
            print "%s" % option_ele.text
            option_ele.click()
            time.sleep(1)

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

 

        



