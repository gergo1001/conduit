from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f

from webdriver_manager.chrome import ChromeDriverManager


class PageMain()
    URL = "http://localhost:1667/"
    registration_link_xpath = '//li[@class="nav-item"]/a[@href="#/register"]'
    driver = None

    def __init__(self, driver=None):
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        else:
            if not f.webpage_lathato:
                browser_options = Options()
                browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
                browser_options.headless = True
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
            else:
                self.driver = driver

    def open(self):
        self.driver.get(self.URL)


def regpage_open(self):
    self.driver.find_element_by_xpath('//li[@class="nav-item"]/a[@href="#/register"]').click()
