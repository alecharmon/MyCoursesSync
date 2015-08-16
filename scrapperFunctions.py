from Models import Course, Document
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
import time
from BeautifulSoup import BeautifulSoup
import re

def login(driver, user, passw):

    driver.get("https://mymcgill.mcgill.ca/portal/page/portal/Login")
    driver.find_element_by_id('username').send_keys(user)
    driver.find_element_by_id('password').send_keys(passw, Keys.RETURN)
    driver.find_element_by_link_text('Access myCourses').click()
    driver.switch_to_window(driver.window_handles[1])
    del driver.window_handles[0]
    ##assert(LogedIn!)


def getCourses(driver,semester):
    ###goes to the main page of my courses and return all classes that have the semester passed in their link as a course obkect
    time.sleep(3)

    courses = []
    links = driver.find_elements_by_partial_link_text(semester)
    for link in links:
        title = link.get_attribute("text")
        x = Course(semester, title, link.get_attribute("href"), link)
        courses.append(x)
    return courses


def getAllDocuments(driver, course):
    driver.get(course.link)
    toRetFolders = []
    driver.find_element_by_link_text('Content').click()
    driver.find_element_by_id('TreeItemTOC').click()
    ## load button does not exit always and does not always apear when it should....
    ## jankey code i know
    try:
        loadMoreButtons = driver.find_element_by_partial_link_text('Load More').click()
        for button in loadMoreButtons:
            button.click()
    except:
        pass

    return scrapeDocuments(driver.page_source,course.title)


def match_class(target):
    target = target.split()
    def do_match(tag):
        try:
            classes = dict(tag.attrs)["class"]
        except KeyError:
            classes = ""
        classes = classes.split()
        return all(c in classes for c in target)
    return do_match

def scrapeDocuments(html,courseTitle):
    soup = BeautifulSoup(html)
    list =  soup.findAll(match_class("d2l-datalist"))
    h2s =  list[0].findAll("h2")
    folders =  list[0].findAll(match_class("d2l-collapsepane-content"))
    documents = []
    for folder, title in zip( folders,  h2s):
        links = folder.findAll('a')
        for link in links:


            if  link.get('href') != "javascript:void(0);" and  link.get('href') != None :
                try:
                    idNumbers  = [int(s) for s in link.get('href').split("/") if s.isdigit()]
                    documentLink = "https://mycourses2.mcgill.ca/d2l/le/content/{0}/topics/files/download/{1}/DirectFileTopicDownload".format(idNumbers[0],idNumbers[1])


                    documentType = docTypes[link.get('title').split(' - ')[-1]]
                    documents.append(Document(link.string, documentLink,documentType, title.string,courseTitle))
                except:
                    print "Unknown Document Type Found"


    return  documents

### a Helper global dictonary for parsing the doc title to the appropriate extenssion
docTypes = {
    'Adobe Acrobat Document': ".pdf",
    'PowerPoint Presentation': ".ppt",
    'Word Document': ".doc",
    'Link Topic': "Link",

}