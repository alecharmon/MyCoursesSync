
from selenium import webdriver
from selhelpers import login

driver = webdriver.Firefox()

##login
login(driver,"shardul.baral@mail.mcgill.ca", "beauties")

driver.quit()

