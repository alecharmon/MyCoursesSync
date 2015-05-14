import os, sys
from selenium import webdriver
from scrapperFunctions import login
from classStructure import Class
from scrapperFunctions import getClasses
import pprint
driver = webdriver.Firefox()

##login
login(driver,"shardul.baral@mail.mcgill.ca", "beauties")
##get classes
classes = getClasses(driver)
##make folders
for x in classes:
	x.makeFolder()

