from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SELECT_ID = (By.NAME, 'Lot')
    ENTRYTIME_NAME = (By.NAME, 'EntryTime')
    RADIO_ID = (By.XPATH, \
            '//input[@name = \'EntryTimeAMPM\'][@value = \'PM\']')
    IMG_ENTRY = (By.XPATH, \
            '//tr[2]/td[2]/font/a/IMG[@ALT = \'Pick a date\']')
    IMG_LEAVE = (By.XPATH, \
            '//tr[3]/td[2]/font/a/IMG[@ALT = \'Pick a date\']')
