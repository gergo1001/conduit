import random
import string

webpage_visible = True

def random_email():
    return "".join([random.choice(string.ascii_lowercase) for _ in range(8)])+'@testemail.hu'

def random_user():
    return "".join([random.choice(string.ascii_letters) for _ in range(6)])

def random_pass():
    return "".join([random.choice(string.ascii_lowercase) for _ in range(6)])+"".join([random.choice(string.ascii_uppercase) for _ in range(1)])+"".join([random.choice(string.digits) for _ in range(1)])+'!'


def inputelement(driver, type, path):
    if type == 'xpath':
        return driver.find_element_by_xpath(path)
