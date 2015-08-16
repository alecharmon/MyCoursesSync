import pprint
from selenium import webdriver
import cookielib
import mechanize
from scraperFunctions import login
from Models import Document
from scrapperFunctions import getCourses,getAllDocuments
import yaml



#using the yaml config
f = open('config.yaml')
config = yaml.load(f)
username = config["mycourses"][0]["user"]
password = config["mycourses"][1]["pass"]
term = config["mycourses"][2]["term"]
path = ""#config["local"][0]["path"]

#start your engines
driver = webdriver.Firefox()
driver.implicitly_wait(5)

#login
login(driver, username, password)
#get classes
classes = getCourses(driver,term)

#get all documents from folders
documents = []
for course in classes:

    courseDocuments = getAllDocuments(driver, course)
    for x in courseDocuments:
        x.course = course.title
        documents.append(x)


# Grab the cookie
cookie = driver.get_cookies()
# Store it in the cookie jar
cj = cookielib.LWPCookieJar()
for s_cookie in cookie:
    cj.set_cookie(cookielib.Cookie(version=0, name=s_cookie['name'], value=s_cookie['value'], port='80', port_specified=False, domain=s_cookie['domain'], domain_specified=True, domain_initial_dot=False, path=s_cookie['path'], path_specified=True, secure=s_cookie['secure'], expires=s_cookie['expiry'], discard=False, comment=None, comment_url=None, rest=None, rfc2109=False))
# Instantiate a Browser and set the cookies
br = mechanize.Browser()
br.set_cookiejar(cj)

#quit driver
driver.close()

# Now open the URL:
for x in documents:
    if x.checkIfFileExists():
        pass#file exits, we are good
    else:
        x.save(br,path)


pass
