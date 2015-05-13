from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver = webdriver.PhantomJS()
driver = webdriver.Firefox()
driver.get("https://mymcgill.mcgill.ca/portal/page/portal/Login")
driver.find_element_by_id('username').send_keys(pw)
driver.find_element_by_id('password').send_keys("",Keys.RETURN)
driver.find_element_by_link_text('Access myCourses').click();
print driver.current_url
