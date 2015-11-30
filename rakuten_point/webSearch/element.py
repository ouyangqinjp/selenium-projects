from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BasePageElement(object):

    def __set__(self, obj, value):
        driver = obj.driver

        print "locator %s" % self.locator
        print "flag %s" % self.flag

        if self.flag == "ByName":
            element = driver.find_element(By.NAME, self.locator)

        if self.flag == "ByXpath":
            element = driver.find_element(By.XPATH, self.locator)

        WebDriverWait(driver, 100).until(lambda driver: element)
        element.clear()
        print "VALUE %s" % value
        element.send_keys(value)

        
    def __get__(self, obj, owner):
        driver = obj.driver

        element = driver.find_element_by_name(self.locator)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        return element

