from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pages.page_registration as p


# In order for ChromeDriverManager to work you must pip install it in your own environment.


def test_registration():
    def van_hibauzenet():
        hibauzenetek = driver.find_elements_by_xpath('/html/body/div[2]')
        if len(hibauzenetek) > 0:
            assert 1 == 1
            hibauzenetek[0].find_element_by_tag_name('button').click()
        else:
            assert 1 == 0

    URL = "http://localhost:1667/"
    ##browser_options = Options()
    # browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # browser_options.headless = True
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    link = driver.find_element_by_xpath('//li[@class="nav-item"]/a[@href="#/register"]')
    link.click()

    preg = p.PageRegistration(driver)
    preg.fill_inputs('h', 'b', 'c')

    time.sleep(20)
    # driver.close()


test_registration()
