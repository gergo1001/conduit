import time

from selenium import webdriver
import pages.func as f
import pages.page_article as a


class PageEditor:
    title_input = ['xpath', '//input[@placeholder="Article Title"]']
    shorttext_input = ['xpath', '//input[@placeholder="What\'s this article about?"]']
    text_input = ['xpath', '//fieldset/textarea[@placeholder="Write your article (in markdown)"]']
    tags_input = ['xpath', "//input[@placeholder='Enter tags']"]
    home_link_xpath = '//li[@class="nav-item"]/a[@href="#/"]'
    button_publish_xpath = '//button'
    def __init__(self, driver):
        self.driver: webdriver = driver
        time.sleep(2)

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
        time.sleep(2)
        return a.PageArticle(self.driver)

    def geturl(self):
        return self.driver.current_url

    def setshorttext(self,shorttext):
        f.inputelement(self.driver, self.shorttext_input[0], self.shorttext_input[1]).clear()
        f.inputelement(self.driver, self.shorttext_input[0], self.shorttext_input[1]).send_keys(shorttext)

    def go_home(self):
        self.driver.find_element_by_xpath(self.home_link_xpath).click()
        time.sleep(1)