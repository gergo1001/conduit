from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f

from webdriver_manager.chrome import ChromeDriverManager


class PageRegistration():
    passw_input = ['xpath', '//input[@placeholder="Password"]']
    email_input = ['xpath', '//input[@placeholder="Email"]']
    user_input = ['xpath', '//input[@placeholder="Username"]']

    def __init__(self, driver=None):
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver = driver

    def fill_inputs(self, user, email, passw):
        f.input_element(self.driver, self.user_input[0], self.user_input[1]).send_keys(user)
        f.input_element(self.driver, self.email_input[0], self.email_input[1]).send_keys(email)
        f.input_element(self.driver, self.passw_input[0], self.passw_input[1]).send_keys(passw)
