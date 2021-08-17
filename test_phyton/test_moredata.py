import pages.page_main as m
import time

def test_moredata():
    p_main = m.PageMain()
    p_main.open()
    p_signin = p_main.signinpage_open()
    #tesztadatok
    testemail='testuser1@example.com'
    testpassw='Abcd123$'
    testuser='testuser1'
    #megadott teszt userrel belépés
    p_signin.fill_inputs(testemail,testpassw )
    p_signin.click_signin()

    time.sleep(4)
    p_main.fill_article()
    p_main.__del__()