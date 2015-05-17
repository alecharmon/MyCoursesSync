from classStructure import Class
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