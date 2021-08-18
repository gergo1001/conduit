import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.page_editor as e
from webdriver_manager.chrome import ChromeDriverManager


class PageArticle:
    title_xpath = '/html/body/div[1]/div/div[1]/div/h1'
    delete_xpath = '/html/body/div[1]/div/div[1]/div/div/span/button/span'
    edit_xpath = '/html/body/div[1]/div/div[1]/div/div/span/a/span'
    shorttext_xpath = ''
    text_xpath = '/html/body/div[1]/div/div[2]/div[1]/div/div[1]/p'
    tags_xpath = '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/a'
    user_xpath = '/html/body/div[1]/div/div[1]/div/div/div/a'
    home_link_xpath = '//li[@class="nav-item"]/a[@href="#/"]'

    def __init__(self, driver):
        self.driver: webdriver = driver

    def getuser(self):
        return self.driver.find_element_by_xpath(self.user_xpath).text

    def gettext(self):
        return self.driver.find_element_by_xpath(self.text_xpath).text

    def gettags(self):
        return self.driver.find_element_by_xpath(self.tags_xpath).text

    def gettitle(self):
        return self.driver.find_element_by_xpath(self.title_xpath).text

    def delete_article(self):
        self.driver.find_element_by_xpath(self.delete_xpath).click()
        time.sleep(1)

    def edit_article(self):
        self.driver.find_element_by_xpath(self.edit_xpath).click()
        time.sleep(1)
        return e.PageEditor(self.driver)

    def back(self):
        self.driver.back()
        time.sleep(1)

    def go_home(self):
        self.driver.find_element_by_xpath(self.home_link_xpath).click()
        time.sleep(1)

    def geturl(self):
        return self.driver.current_url
