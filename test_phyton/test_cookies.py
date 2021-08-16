from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pages.page_registration as p
import pages.page_main as m
import pages.func as f


def test_cookies():
    p_main = m.PageMain()
    p_main.open()

    #ha nincs cookie, akkor láthatónak kellene lennie, ez időnként elbukik
    if p_main.getcookies() == "":
        assert p_main.cookies_button_visible() is True

    #törli a cookiekat
    p_main.deletecookies()
    p_main.open()
    # gombok láthatóak-e
    assert p_main.cookies_button_visible() is True
    p_main.cookies_website_click()

    #jó oldalra visz e a cookies link
    assert p_main.get_and_close_second_window_url() == "https://www.cookiesandyou.com/"

    time.sleep(20)
    p_main.cookies_accept()
    assert p_main.getcookies() == 'accept'

    p_main.open()
    #gomboknak nem kell már láthatónak lennie
    assert p_main.cookies_button_visible() is False

    p_main.deletecookies()
    p_main.open()
    #gombok láthatóak-e
    assert p_main.cookies_button_visible() is True
    p_main.cookies_decline()
    assert p_main.getcookies() == 'decline '

