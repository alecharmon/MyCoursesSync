from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(user, passw):
	driver = webdriver.Firefox()
	driver.get("https://mymcgill.mcgill.ca/portal/page/portal/Login")
	driver.find_element_by_id('username').send_keys(user)
	driver.find_element_by_id('password').send_keys(passw, Keys.RETURN)
	driver.find_element_by_link_text('Access myCourses').click();
	return driver.current_url

print(login("shardul.baral@mail.mcgill.ca", "beauties"))

