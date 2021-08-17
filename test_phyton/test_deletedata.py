import pages.func as f
import pages.page_main as m
import time

def test_deletedata():
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

        title = f.random_title()
        stext = 'blabla'
        text = 'caaaa'
        tags = 'dssss'

        p_editor = p_main.newarticlepage_open()
        p_editor.fill_inputs(title, stext, text, tags)

        p_article = p_editor.click_publish()
        time.sleep(2)
        assert testuser == p_article.getuser()
        assert text == p_article.gettext()
        assert tags == p_article.gettags()
        assert title == p_article.gettitle()
        p_article.delete_article()
        time.sleep(2)
        p_article.go_home()
        time.sleep(2)
        #felgyűjti újra az összes cikket és ellenőrzi, hogy az a tittle ne legyen közötte
        assert p_main.search_article_with_title(title) is False
    finally:
        p_main.__del__()
