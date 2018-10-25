
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException,TimeoutException,StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def retryingFindClick(by,driver):
    result = False
    attempts = 0
    while attempts < 2:
        try:
            driver.find_element_by_xpath(by).click()
            result = True
            break
        except StaleElementReferenceException as e :
            pass
        attempts+=1
        return result

def input_driver (driver,value,xpath):
    if value=="":
        pass
    else:
        driver.find_element_by_xpath(xpath).clear()
        driver.find_element_by_xpath(xpath).send_keys(value)

def select_driver (driver,value,xpath):
    if value=="":
        pass
    else:
        driver.find_element_by_xpath(xpath).click()
        time.sleep(0.3)
        class_name =driver.find_element_by_xpath(xpath+'/../..').get_attribute("class") 
        driver.find_element_by_xpath("//span[@class='%s'][contains(text(),'%s')]" % (class_name[:12],value)).click()
        time.sleep(0.3)

def radio_driver(driver,value,xpath):
    if value=="":
        pass
    else:
        driver.find_element_by_xpath(xpath.replace('?', value)).click()
        

