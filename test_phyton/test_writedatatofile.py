import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f
import pages.page_registration as p
import pages.page_signin as s
import pages.page_main as m
import pages.page_editor as e
import pages.page_article as a
import time


def test_datawritetofile():
    p_main = m.PageMain()
    p_main.open()
    time.sleep(2)
    p_signin = p_main.signinpage_open()
    time.sleep(2)
    # tesztadatok
    testemail = 'testuser1@example.com'
    testpassw = 'Abcd123$'
    testuser = 'testuser1'
    # megadott teszt userrel belépés
    p_signin.fill_inputs(testemail, testpassw)
    p_signin.click_signin()
    time.sleep(2)
    p_main.articles_write_to_file('output.csv')
    p_main.__del__()

