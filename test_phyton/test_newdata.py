import pages.page_main as m
import time


def test_newdata():
    p_main = m.PageMain()
    p_main.open()
    try:
        p_signin = p_main.signinpage_open()
        # tesztadatok
        testemail = 'testuser1@example.com'
        testpassw = 'Abcd123$'
        testuser = 'testuser1'
        # megadott teszt userrel belépés
        p_signin.fill_inputs(testemail, testpassw)
        p_signin.click_signin()

        title = 'a'
        stext = 'blabla'
        text = 'caaaa'
        tags = 'dssss'

        p_editor = p_main.newarticlepage_open()
        p_editor.fill_inputs(title, stext, text, tags)

        p_article = p_editor.click_publish()
        assert testuser == p_article.getuser()
        assert text == p_article.gettext()
        assert tags == p_article.gettags()
        assert title == p_article.gettitle()
        p_article.back()
        print('1 test ok')
        # ugyanazzal a title-l nem szabadna, 2* elfogadni
        title = 'a'
        stext = 'blabla2'
        text = 'caaaa2'
        tags = 'dssss2'

        p_editor = p_main.newarticlepage_open()
        p_editor.fill_inputs(title, stext, text, tags)

        p_article = p_editor.click_publish()
        assert testuser == p_article.getuser()
        assert text == p_article.gettext()
        assert tags == p_article.gettags()
        assert title == p_article.gettitle()
        time.sleep(2)
        print('2 test ok')
    finally:
        p_main.__del__()
