import pages.func as f
import pages.page_main as m
import time

def test_editdata():
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

    title = f.random_title()
    stext = 'blabla'
    text = 'caaaa'
    tags = 'dssss'

    p_editor = p_main.newarticlepage_open()
    p_editor.fill_inputs(title, stext, text, tags)

    p_article = p_editor.click_publish()
    time.sleep(2)

    p_editor=p_article.edit_article()
    time.sleep(1)
    ujertek="ujertek"

    p_editor.setshorttext(ujertek)
    p_editor.click_publish()
    p_editor.go_home()
    time.sleep(2)
    #felgyűjti újra az összes cikket és ellenőrzi, hogy az adott tittle-el rendelkező cikknél az új érték e a shorttext
    assert p_main.article_shorttext_van(title,ujertek) is True
    p_main.__del__()


