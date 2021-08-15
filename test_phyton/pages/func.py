def input_element(driver,type,eleres):
    if type=='xpath':
        return driver.find_element_by_xpath(eleres)