webpage_visible = True


def inputelement(driver, type, path):
    if type == 'xpath':
        return driver.find_element_by_xpath(path)
