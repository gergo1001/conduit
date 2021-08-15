from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pages.page_registration as p
import pages.page_main as m


# In order for ChromeDriverManager to work you must pip install it in your own environment.


def test_registration():
    URL = "http://localhost:1667/"

    p_main = m.PageMain()
    p_main.open()
    p_reg=p_main.regpage_open()
    p_reg.fill_inputs('h','a','b')
    time.sleep(20)
    # driver.close()


test_registration()
