import pprint
from selenium import webdriver

from scrapperFunctions import login
from classStructure import folderFile, classFolder
from scrapperFunctions import getClasses,getFolder


driver = webdriver.Firefox()
driver.implicitly_wait(5)
##login
login(driver, "shardul.baral@mail.mcgill.ca", "beauties")
##get classes
classes = getClasses(driver)
##make folders

classFolder = getFolder(driver, classes[0])
pp = pprint.PrettyPrinter(indent=4)
for x in classFolder:
    print(x.title+"__________")
    x.makeFolder()

    for y in x.links:
       y.getFile(driver,x)
# for x in classes:
#     x.makeFolder()


    # driver.get(x.link)
    # driver.find_element_by_link_text('Content').click()
    # folders = driver.find_elements_by_class_name('d2l-datalist')
    # headings = folders[0].find_elements_by_xpath(".//h2")
    # del folders[0]
    # for folder in folders:
    #     heading = headings[0].get_attribute("innerHTML")
    #     del headings[0]
    #     scraperLinks = folder.find_elements_by_xpath(".//a")
    #     links =[]
    #     for y in scraperLinks:
    #         if (y.get_attribute("text") != "" ) &  (y.get_attribute("innerHTML").find("<img") < 0):
    #             tempLink = folderFile(y.get_attribute("innerHTML"),y.get_attribute("Href"))
    #             links.append(tempLink)
    #     temp= classFolder(heading,links)
    #     print("test")


# for x in xrange(0,len(folders)-1):
# 	temp = driver.find_elements_by_class_name('d2l-datalist-item-content')
# 	print temp[x].find_element_by_class_name("d2l-heading").get_attribute("innerHTML")
# 	driver.find_element_by_link_text('Content').click()
# heading = folder.find_element_by_class_name("d2l-heading")
# print heading.get_attribute("innerHTML")
# links = folder.find_elements_by_class_name("d2l-link")
# for link in links:
# 	print link.get_attribute("text")
# 	pass

# pass


# driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]")
# iframe = driver.find_elements_by_tag_name('iframe')[0]
# driver.switch_to_frame(iframe)
# links=driver.find_elements_by_class_name('ddl_li_c')
# recNavigate(driver,links )
	

