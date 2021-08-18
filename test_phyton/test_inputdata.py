import csv
import pages.page_main as m


def test_inputdata():
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
        tittles = []
        with open('./test_phyton/input.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            next(reader)
            for row in reader:
                p_editor = p_main.newarticlepage_open()
                tittles.append(row[0])
                p_editor.fill_inputs(row[0], row[1], row[2], row[3])
                p_editor.click_publish()
        p_editor.go_home()
        upload_element_count = len(tittles)
        checked_upload = 0
        for tittle in tittles:
            if p_main.search_article_with_title(tittle):
                checked_upload += 1
        # ellenőrzi, hogy mindegyik feltöltésre került
        assert upload_element_count == checked_upload

        # kitörtli a felvitt adatokat
        for tittle in tittles:
            p_main.del_article(tittle, False)
    finally:
        p_main.__del__()



