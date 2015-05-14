from classStructure import Class

def getClasses(driver):
	classes = []
	links = driver.find_elements_by_partial_link_text("Fall 2013")
	for link in links:
	    title = link.get_attribute("text")
	    title = title.split('-')
	    title = title[-1]
	    x = Class("Fall 2013",title,link.get_attribute("href"))
	    classes.append(x)
	return classes