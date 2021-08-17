import pages.func as f
import pages.page_main as m
import pages.class_article as ca


def test_new_tittle_only_once():
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
        articles = []
        tittles = []
        tag = 'c'
        #cikkeket generál
        for _ in range(3):
            tittle = f.random_title()
            if tittle not in tittles:
                article = ca.Article(None, tittle, 'a', 'b', tag)
                articles.append(article)
                tittles.append(tittle)
        for article in articles:
            p_editor = p_main.newarticlepage_open()
            p_editor.fill_inputs(article.gettitle(), article.shorttext, article.text, tag)
            p_article = p_editor.click_publish()
            article.setlink(p_article.geturl())
            p_article.go_home()
        #összegyűjti az összes cikket, és megnézi, hogy nincs ismétlé
        assert p_main.none_repeat_tittle_from_list_article(tittles) is True
        #megnyitja egyesével a cikkeket, és törli
        for article in articles:
            p_article = p_main.article_open(article.link)
            p_article.delete_article()
    finally:
        p_main.__del__()
