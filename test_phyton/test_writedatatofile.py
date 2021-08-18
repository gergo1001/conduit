import pages.page_main as m


def test_datawritetofile():
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
    article_count = p_main.get_article()
    write_article = p_main.articles_write_to_file('./test_phyton/output.csv')
    assert article_count == write_article
