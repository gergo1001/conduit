import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f

from webdriver_manager.chrome import ChromeDriverManager

class PageSignin():
    passw_input = ['xpath', '//input[@placeholder="Password"]']
    email_input = ['xpath', '//input[@placeholder="Email"]']
    button_signin_xpath = '//button'

    def fill_inputs(self, email, passw):

        f.inputelement(self.driver, self.email_input[0], self.email_input[1]).clear()
        f.inputelement(self.driver, self.email_input[0], self.email_input[1]).send_keys(email)
        f.inputelement(self.driver, self.passw_input[0], self.passw_input[1]).clear()
        f.inputelement(self.driver, self.passw_input[0], self.passw_input[1]).send_keys(passw)

    def click_signin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def __init__(self, driver=None):
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver : webdriver = driver