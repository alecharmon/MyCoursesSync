from classStructure import course, Document, courseFolder
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
        x = course(semester, title, link.get_attribute("href"), link)
        courses.append(x)
    return courses


def getDirectory(driver, course):
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

    folders = getAllFolders(driver.page_source)


    ## within a course directory there are subfolders
    # folders = driver.find_elements_by_class_name('d2l-datalist')
    # headings = folders[0].find_elements_by_xpath(".//h2")
    # ## the first folder is genereric and does not have a link
    # del folders[0]
    #
    # for folder in folders:
    #     heading = headings[0].get_attribute("innerHTML")
    #     del headings[0]
    #     getAllATags(heading)
    #     ## scrapper links are the selenium drier objecrs and document links are the parsed python object
    #
    #     scraperLinks = folder.find_elements_by_xpath(".//a")
    #     documentLinks = []
    #     for scraperlink in scraperLinks:
    #         ##filtering out mycourses wierdness
    #         # if (scraperlink.get_attribute("text") != "" ) & (scraperlink.get_attribute("innerHTML").find("<img") < 0):
    #         #     documentLinks.append(Document(scraperlink.get_attribute("innerHTML"), scraperlink.get_attribute("Href")))
    #         #     pass
    #         pass
    #
    #     toRetFolders.append(courseFolder(heading, documentLinks, course.title))
    # return toRetFolders
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

def getAllFolders(html):
    soup = BeautifulSoup(html)
    list =  soup.findAll(match_class("d2l-datalist"))
    h2s =  list[0].findAll("h2")
    folders =  list[0].findAll(match_class("d2l-collapsepane-content"))
    print len(folders),  "  " ,len(h2s)
    tstzip = zip( folders,  h2s)
    print len(tstzip)
    for folder, title in zip( folders,  h2s):
        print title.string
        links = folder.findAll('a')

        for link in links:

            if  link.get('href') != "javascript:void(0);" and  link.get('href') != None :
                print link.get('href')


    return  folders
    # for link in soup.findAll(match_class("d2l-datalist")):
    #     print link.get('href')
    #

    pass

