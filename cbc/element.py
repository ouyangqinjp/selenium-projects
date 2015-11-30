from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class BasePageElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        element = driver.find_element_by_name(self.locator)
        WebDriverWait(driver, 100).until(
            lambda driver: element)
        element.clear()
        print "VALUE %s" % value
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver

        element = driver.find_element_by_name(self.locator)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        return element

class SearchPageElement(object):
    def __get__(self, obj, owner):
        driver = obj.driver

        element = driver.find_element_by_tag_name(self.locator)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_tag_name(self.locator))
        return element
        """
        i = 0
        for i in xrange(len(elements)):
            i = i + 1
            print "i = %s" % i
            print "element %s" % elements[i].text
        #return elemens[i]



        #print "ESESES %s " % type(elements).__name__
        #print "ESESES len %s " % len(elements)


        #WebDriverWait(driver, 100).until(
        #    lambda driver: driver.find_element_by_tag_name(self.locator))
        """


    
