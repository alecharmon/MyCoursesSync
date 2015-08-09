import os, sys
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

class link:
    def __init__(self, semster, title, link):
        self.semster = semster
        self.title = title
        self.link = link


class course:
    def __init__(self, semster, title, link, element):
        self.semster = semster
        self.title = title
        self.link = link
        self.element = element

    def makeFolder(self):
        if not os.path.exists("testing/" + self.title):
            os.mkdir("testing/" + self.title)


class courseFolder:
    def __init__(self, title, links, Classname):
        self.title = title
        self.links = links
        self.className = Classname


    def makeFolder(self):
        if not os.path.exists("testing/" + self.className+"/"+ self.title):
            os.mkdir("testing/" +self.className+"/"+ self.title)


class Document:
    def __init__(self, title, link):
        self.title = title
        self.link = link
    def saveFile(self,driver, folder):
        ##check if file exits
        if(os.path.isfile("testing/" +folder.className+"/"+ folder.title+"/"+self.title)):
            #iff it does skip
            pass
        else:
            driver.get(self.link)
            try:
                toDownloadfile = driver.find_element_by_class_name("d2l-fileviewer-pdf")
                link = toDownloadfile.get_attribute("data-location")
                print ("https://mycourses2.mcgill.ca"+link)
            except:
                driver.find_element_by_partial_link_text('Open in New Window').click()
                driver.switch_to_window(driver.window_handles[1])
                link = driver.current_url
                driver.switch_to_window(driver.window_handles[1])
                del driver.window_handles[1]
                print(link)



        #else download it

        # selnium does not have any real way of downloading files in the background, phantomjs 
        # does not have any form of downloading in the realase i was working with
        pass


		




