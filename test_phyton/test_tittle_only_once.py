import pages.page_main as m
import time

def test_tittle_only_once():
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
        assert p_main.none_repeat_tittle() is True
    finally:
        p_main.__del__()