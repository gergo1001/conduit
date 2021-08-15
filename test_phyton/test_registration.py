from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pages.page_registration as p
import pages.page_main as m
import pages.func as f



# In order for ChromeDriverManager to work you must pip install it in your own environment.


def test_registration():
    p_main = m.PageMain()
    p_main.open()
    p_reg = p_main.regpage_open()

    p_reg.fill_inputs(f.random_user(), "", f.random_pass())
    p_reg.click_registration()
    assert p_reg.good_message_missing_email == p_reg.get_message()

    p_reg.fill_inputs(f.random_user(), f.random_email(), f.random_pass())
    p_reg.click_registration()
    assert p_reg.good_message_ok == p_reg.get_message()


    p_main.__del__()



