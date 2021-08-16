from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f
import pages.page_registration as p
import pages.page_signin as s
import pages.page_main as m
import pages.page_editor as e
import time

def test_newdata():
    p_main = m.PageMain()
    p_main.open()
    p_signin = p_main.signinpage_open()
    #megadott teszt userrel belépés
    p_signin.fill_inputs('testuser1@example.com', 'Abcd123$')
    p_signin.click_signin()

    p_editor = p_main.newarticlepage_open()
    p_editor.fill_inputs('a','b','c','d')

    time.sleep(4)

test_newdata()