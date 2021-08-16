from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f
import pages.page_registration as p
import pages.page_signin as s
import pages.page_main as m
import pages.page_editor as e
import pages.page_article as a
import pages.class_article as ca
import time

def test_new_tittle_only_once():
    p_main = m.PageMain()
    p_main.open()
    p_signin = p_main.signinpage_open()
    # tesztadatok
    testemail = 'testuser1@example.com'
    testpassw = 'Abcd123$'
    testuser = 'testuser1'
    # megadott teszt userrel belépés
    p_signin.fill_inputs(testemail, testpassw)
    p_signin.click_signin()
    time.sleep(2)
    articles=[]
    tittles=[]
    tag='c'
    for _ in range(3):
        tittle=f.random_title()
        if tittle not in tittles:
            article=ca.Article(None,tittle,'a','b',tag)
            articles.append(article)
            tittles.append(tittle)
    for article in articles:
        p_editor = p_main.newarticlepage_open()
        p_editor.fill_inputs(article.gettitle(), article.shorttext, article.text, tag)
        p_article = p_editor.click_publish()
        article.setlink(p_article.geturl())
        p_article.go_home()
        time.sleep(1)

    #assert p_main.none_repeat_tittle_from_list_article(tittles) is True

    for article in articles:
        p_article=p_main.article_open(article.link)
        p_article.delete_article()
        time.sleep(3)

    p_main.__del__()
