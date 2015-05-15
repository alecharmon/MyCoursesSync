import os, sys
from selenium import webdriver
from scrapperFunctions import login
from classStructure import Class
from scrapperFunctions import getClasses
import pprint
import time
# def recNavigate(driver, links):
# 	for x in links:
# 		try:
# 			x.click()
		
# 		except: 
#   			pass
# 		link driver.find_elements_by_css_selector("li")
		
		# subSections = driver.find_elements_by_class_name('ddl_li_c')
		# for y in subSections:
		# 	print y.get_attribute("text")
		# driver.switch_to_frame(iframe)
driver = webdriver.Firefox()

##login
login(driver,"shardul.baral@mail.mcgill.ca", "beauties")
##get classes
classes = getClasses(driver)
##make folders
for x in classes:
	x.makeFolder()
	driver.get(x.link)
	driver.find_element_by_link_text('Content').click()
	element = driver.find_element_by_class_name('d2l-datalist')
	print element.get_attribute('innerHTML')


	
	# driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]")
	# iframe = driver.find_elements_by_tag_name('iframe')[0]
	# driver.switch_to_frame(iframe)
	# links=driver.find_elements_by_class_name('ddl_li_c')
	# recNavigate(driver,links )
	

