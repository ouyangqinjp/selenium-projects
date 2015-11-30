from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.ID, 'login_link')
    SUBMIT_BUTTON = (By.NAME, 'submit')
    SEARCH_BUTTON = (By.ID, 'sBtn')

    SPAN_ID = (By.ID, 'topArea')

    ENTRYTIME_NAME = (By.NAME, 'EntryTime')
    RADIO_ID = (By.XPATH, \
            '//input[@name = \'EntryTimeAMPM\'][@value = \'PM\']')
    IMG_ENTRY = (By.XPATH, \
            '//tr[2]/td[2]/font/a/IMG[@ALT = \'Pick a date\']')
    IMG_LEAVE = (By.XPATH, \
            '//tr[3]/td[2]/font/a/IMG[@ALT = \'Pick a date\']')
