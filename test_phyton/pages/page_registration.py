import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f

from webdriver_manager.chrome import ChromeDriverManager




class PageRegistration():
    passw_input = ['xpath', '//input[@placeholder="Password"]']
    email_input = ['xpath', '//input[@placeholder="Email"]']
    user_input = ['xpath', '//input[@placeholder="Username"]']
    link_registration_xpath='//button'
    message_text_xpath='/html/body/div[2]/div/div[2]'
    message_ok_xpath='/html/body/div[2]/div/div[4]/div/button'
    good_message_ok='Welcome!'
    good_message_missing_email='Registration failed!'
    def __init__(self, driver=None):
        if driver == None:
            options = Options()
            options.headless = False
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver : webdriver = driver

    def fill_inputs(self, user, email, passw):
        f.inputelement(self.driver, self.user_input[0], self.user_input[1]).clear()
        f.inputelement(self.driver, self.user_input[0], self.user_input[1]).send_keys(user)
        f.inputelement(self.driver, self.email_input[0], self.email_input[1]).clear()
        f.inputelement(self.driver, self.email_input[0], self.email_input[1]).send_keys(email)
        f.inputelement(self.driver, self.passw_input[0], self.passw_input[1]).clear()
        f.inputelement(self.driver, self.passw_input[0], self.passw_input[1]).send_keys(passw)

    def click_registration(self):
        self.driver.find_element_by_xpath(self.link_registration_xpath).click()

    def get_message(self):
        time.sleep(2)
        message=self.driver.find_element_by_xpath(self.message_text_xpath).text
        time.sleep(2)
        self.driver.find_element_by_xpath(self.message_ok_xpath).click()
        print(message)
        return message
    # def van_hibauzenet():
    #    hibauzenetek = driver.find_elements_by_xpath('/html/body/div[2]')
    #    if len(hibauzenetek) > 0:
    #        assert 1 == 1
    #        hibauzenetek[0].find_element_by_tag_name('button').click()
    #    else:
    #        assert 1 == 0
