from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f

from webdriver_manager.chrome import ChromeDriverManager


class PageMain():
    URL = "http://localhost:1667/"
    registration_link_xpath = '//li[@class="nav-item"]/a[@href="#/register"]'
    driver = None

    def __init__(self):
        if not f.webpage_lathato:

            browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
            browser_options.headless = True
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

        else:
            browser_options = Options()
            browser_options.headless = False
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

    def open(self):
        self.driver.get(self.URL)

    def regpage_open(self):
        self.driver.find_element_by_xpath('//li[@class="nav-item"]/a[@href="#/register"]').click()

    def __del__(self):
        self.driver.close()
        self.driver.quit()