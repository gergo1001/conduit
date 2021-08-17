import random
import string

webpage_visible = False


def random_email():
    return "".join([random.choice(string.ascii_lowercase) for _ in range(8)]) + '@testemail.hu'


def random_user():
    return "".join([random.choice(string.ascii_letters) for _ in range(6)])


def random_pass():
    return "".join([random.choice(string.ascii_lowercase) for _ in range(6)]) + "".join(
        [random.choice(string.ascii_uppercase) for _ in range(1)]) + "".join(
        [random.choice(string.digits) for _ in range(1)]) + '!'


def random_title():
    return "".join([random.choice(string.ascii_letters) for _ in range(10)])


def inputelement(driver, typeofelementpath, path):
    if typeofelementpath == 'xpath':
        return driver.find_element_by_xpath(path)
