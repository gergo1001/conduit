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
    p_main.articles_write_to_file('./output.csv')
