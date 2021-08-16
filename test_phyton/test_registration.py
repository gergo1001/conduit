from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pages.page_registration as p
import pages.page_main as m
import pages.func as f



# In order for ChromeDriverManager to work you must pip install it in your own environment.

#sign up, logout, login funkció tesztelése
def test_registration():
    p_main = m.PageMain()
    p_main.open()
    p_reg = p_main.regpage_open()

    #regisztráció üres email cimmel
    p_reg.fill_inputs(f.random_user(), "", f.random_pass())
    p_reg.click_registration()
    assert p_reg.good_message_missing_email == p_reg.get_message()
    #regisztráció helyes adatokkal
    user = f.random_user()
    email=f.random_email()
    password=f.random_pass()
    p_reg.fill_inputs(user, email , password)
    p_reg.click_registration()
    assert p_reg.good_message_ok == p_reg.get_message()
    time.sleep(4)
    assert p_main.get_user_sign_in(user) is True
    # kijelentkezés
    p_main.logout_click()
    time.sleep(3)
    assert p_main.get_user_sign_in(user) is False

    #bejelentkezés
    p_signin = p_main.signinpage_open()
    p_signin.fill_inputs(email, password)
    p_signin.click_signin()
    time.sleep(4)
    assert p_main.get_user_sign_in(user) is True


    p_main.__del__()


