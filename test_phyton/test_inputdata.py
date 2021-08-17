import csv
import pages.page_main as m
import time


def test_inputdata():
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
    time.sleep(1)
    with open('./test_phyton/input.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)
        for row in reader:
            p_editor = p_main.newarticlepage_open()
            print(len(row))
            print(row)
            p_editor.fill_inputs(row[0], row[1], row[2], row[3])
            p_editor.click_publish()
            time.sleep(2)

