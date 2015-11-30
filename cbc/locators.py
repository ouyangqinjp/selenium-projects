from selenium.webdriver.common.by import By

class MainPageLocators(object):
    CONTENTS = (By.XPATH, \
            '//div[@id=\'hp-feature-hero\']')
    LOCAL_BUTTON = (By.XPATH, \
            '//nav[@id=\'cbc-globalnav\']/div[1]/ul[1]/li[7]/button')
    MORE_BUTTON = (By.XPATH, \
            '//nav[@id=\'cbc-globalnav\']/div[1]/ul[1]/li[8]/button')
    LOGIN_BUTTON = (By.XPATH, \
            '//nav[@id=\'cbc-globalnav\']/div[1]/ul[2]/li[3]/button')
    GO_BUTTON = (By.NAME, 'gns')
    FB_BUTTON = (By.ID, 'vf-facebook-login')
    SELECT_BUTTON = (By.NAME, 'radio-select')
    SELECT_GO_BUTTON = (By.CLASS_NAME, 'submit')
    SELECT_LISTEN_BUTTON = (By.CLASS_NAME, 'listen-live')
    TABLE = (By.CLASS_NAME, 'networkschedule')
    TV_GO_BUTTON = (By.XPATH, \
            '//ul/li[1]')

class SearchResultsPageLocators(object):
    IFRAME = (By.XPATH, '//iframe[@id=\'searchFrame\']')
    NEXT_PAGE_BUTTON = (By.XPATH, \
            '//div[@id=\'bottom-navigation\']/center/div/table/tbody/tr/td[8]/span/a')
    TABLE = (By.XPATH, '//div[@id=\'bottom-navigation\']/center/div/table')
    GO_BUTTON = (By.NAME, 'btnG')
