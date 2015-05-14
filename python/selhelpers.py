from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def login(driver, user, passw):
	driver.get("https://mymcgill.mcgill.ca/portal/page/portal/Login")
	driver.find_element_by_id('username').send_keys(user)
	driver.find_element_by_id('password').send_keys(passw, Keys.RETURN)
    	driver.find_element_by_link_text('Access myCourses').click()
	driver.switch_to_window(driver.window_handles[1])
	time.sleep(10)

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 15:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )

class wait_for_page_load(object):

    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        self.old_page = self.driver.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.driver.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)
