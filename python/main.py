import os, sys
from selenium import webdriver
from scrapperFunctions import login
from classStructure import Class
from scrapperFunctions import getClasses
import pprint
import time

driver = webdriver.Firefox()

##login
login(driver,"shardul.baral@mail.mcgill.ca", "beauties")
##get classes
classes = getClasses(driver)
##make folders
for x in classes:
	x.makeFolder()
	driver.get(x.link)
	time.sleep(2)
	iframe = driver.find_elements_by_tag_name('iframe')[0]
	driver.switch_to_frame(iframe)
	#driver.find_element_by_class_name('ddl_sc').get_attribute('innerHTML')
	# time.sleep(2)
	sections = driver.find_elements_by_class_name('ddl_li_c')
	for x in sections:
		print x.get_attribute("text")