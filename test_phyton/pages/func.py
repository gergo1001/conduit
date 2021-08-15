webpage_visible=False

def input_element(driver,type,path):
    if type=='xpath':
        return driver.find_element_by_xpath(path)