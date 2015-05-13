
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selhelpers import wait_for_page_load

driver = webdriver.Firefox()


def login(user, passw):
	driver.get("https://mymcgill.mcgill.ca/portal/page/portal/Login")
	driver.find_element_by_id('username').send_keys(user)
	driver.find_element_by_id('password').send_keys(passw, Keys.RETURN)
	
    	driver.find_element_by_link_text('Access myCourses').click();
	driver.switch_to_window(driver.window_handles[1])
	time.sleep(10)
	return driver.current_url

print(login("shardul.baral@mail.mcgill.ca", "beauties"))
driver.quit()
