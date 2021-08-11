from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# In order for ChromeDriverManager to work you must pip install it in your own environment.

def test_registration():

    URL = "http://localhost:1667/"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=browser_options)
    driver.get(URL)

    link=driver.find_element_by_xpath('//li[@class="nav-item"]/a[@href="#/register"]')

    link.click()
    assert 1==1
    driver.close()

