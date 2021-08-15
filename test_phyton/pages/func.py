import random
import string

webpage_visible = False

def random_email():
    return "".join([random.choice(string.ascii_lowercase) for _ in range(8)])+'@testemail.hu'

def random_user():
    return 'bela'

def random_pass():
    return '789456Abcd!'


def inputelement(driver, type, path):
    if type == 'xpath':
        return driver.find_element_by_xpath(path)
