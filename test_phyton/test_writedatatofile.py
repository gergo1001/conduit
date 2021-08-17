import pages.page_main as m
import time


def test_datawritetofile():
    p_main = m.PageMain()
    p_main.open()
    time.sleep(2)
    p_signin = p_main.signinpage_open()
    time.sleep(2)
    # tesztadatok
    testemail = 'testuser1@example.com'
    testpassw = 'Abcd123$'
    testuser = 'testuser1'
    # megadott teszt userrel belépés
    p_signin.fill_inputs(testemail, testpassw)
    p_signin.click_signin()
    time.sleep(2)
    p_main.articles_write_to_file('./test_phyton/output.csv')
    p_main.__del__()

