import pages.page_main as m


def test_moredata():
    try:
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
        page_count = p_main.get_pages_count()
        bejart_lap = p_main.fill_article()

        # leellenorzi, hogy minden lapot sikerult e bejarni
        assert page_count == bejart_lap
    finally:
        p_main.__del__()


