import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f
import pages.page_article as a

from webdriver_manager.chrome import ChromeDriverManager

class PageEditor():
    title_input = ['xpath', '//input[@placeholder="Article Title"]']
    shorttext_input = ['xpath', '//input[@placeholder="What\'s this article about?"]']
    text_input = ['xpath', '//fieldset/textarea[@placeholder="Write your article (in markdown)"]']
    tags_input = ['xpath', "//input[@placeholder='Enter tags']"]

    button_publish_xpath = '//button'
    def __init__(self, driver=None):
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver: webdriver = driver

    def fill_inputs(self, title, shorttext,text,tags):
        f.inputelement(self.driver, self.title_input[0], self.title_input[1]).clear()
        f.inputelement(self.driver, self.title_input[0], self.title_input[1]).send_keys(title)
        f.inputelement(self.driver, self.shorttext_input[0], self.shorttext_input[1]).clear()
        f.inputelement(self.driver, self.shorttext_input[0], self.shorttext_input[1]).send_keys(shorttext)
        f.inputelement(self.driver, self.text_input[0], self.text_input[1]).clear()
        f.inputelement(self.driver, self.text_input[0], self.text_input[1]).send_keys(text)
        f.inputelement(self.driver, self.tags_input[0], self.tags_input[1]).clear()
        f.inputelement(self.driver, self.tags_input[0], self.tags_input[1]).send_keys(tags)

    def click_publish(self):
        self.driver.find_element_by_xpath(self.button_publish_xpath).click()
        return a.PageArticle(self.driver)