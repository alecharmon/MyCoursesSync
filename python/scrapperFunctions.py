from classStructure import Class,folderFile,classFolder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
import time


def login(driver, user, passw):
    driver.get("https://mymcgill.mcgill.ca/portal/page/portal/Login")
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password').send_keys(passw, Keys.RETURN)
    driver.find_element_by_link_text('Access myCourses').click()
    driver.switch_to_window(driver.window_handles[1])


def getClasses(driver):
    classes = []
    links = driver.find_elements_by_partial_link_text("Fall 2013")
    for link in links:
        title = link.get_attribute("text")
        # title = title.split('-')
        # title = title[1]
        x = Class("Fall 2013", title, link.get_attribute("href"), link)
        classes.append(x)
    return classes

def getFolder(driver, Class ):
    driver.get(Class.link)
    toRetFolders=[]
    driver.find_element_by_link_text('Content').click()
    folders = driver.find_elements_by_class_name('d2l-datalist')
    headings = folders[0].find_elements_by_xpath(".//h2")
    del folders[0]
    for folder in folders:
        heading = headings[0].get_attribute("innerHTML")
        del headings[0]
        scraperLinks = folder.find_elements_by_xpath(".//a")
        links =[]
        for y in scraperLinks:
            if (y.get_attribute("text") != "" ) &  (y.get_attribute("innerHTML").find("<img") < 0):
                tempLink = folderFile(y.get_attribute("innerHTML"),y.get_attribute("Href"))
                links.append(tempLink)
        temp= classFolder(heading,links)
        toRetFolders.append(temp)
    return toRetFolders
