import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f

from webdriver_manager.chrome import ChromeDriverManager
class PageArticle():
    title_xpath = '/html/body/div[1]/div/div[1]/div/h1'
    shorttext_xpath = ''
    text_xpath = '/html/body/div[1]/div/div[2]/div[1]/div/div[1]/p'
    tags_xpath = '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/a'
    user_xpath = '/html/body/div[1]/div/div[1]/div/div/div/a'

    def __init__(self, driver=None):
        time.sleep(2)
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver: webdriver = driver

    def getuser(self):
        return self.driver.find_element_by_xpath(self.user_xpath).text

    def gettext(self):
        return self.driver.find_element_by_xpath(self.text_xpath).text

    def gettags(self):
        return self.driver.find_element_by_xpath(self.tags_xpath).text

    def gettitle(self):
        return self.driver.find_element_by_xpath(self.title_xpath).text