from selenium import webdriver
from selhelpers import login
from classStructure import Class
from scrapperFunctions import getClasses
import pprint
driver = webdriver.Firefox()

##login
login(driver,"shardul.baral@mail.mcgill.ca", "beauties")
classes = getClasses(driver)
