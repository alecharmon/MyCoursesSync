import pprint
from selenium import webdriver

from scrapperFunctions import login
from classStructure import Document, courseFolder
from scrapperFunctions import getCourses,getDirectory


driver = webdriver.Firefox()
driver.implicitly_wait(5)
##login
username = "alec.blumenfeld@mail.mcgill.ca"
password = "Sora1900"
login(driver, username, password)
##get classes
classes = getCourses(driver,"Fall 2013")

##make folders
courseFolders = getFolder(driver, classes[0])

for folder in courseFolders:
    print(folder.title+"__________")
    folder.makeFolder()

    for y in folder.links:
       y.getFile(driver,folder)


for x in classes:
    x.makeFolder()

