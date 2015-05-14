import os, sys
from selenium import webdriver
class link:
	def __init__(self, semster, title, link):
		self.semster =semster
		self.title = title
		self.link =link


class Class:
	def __init__(self, semster, title,link, element):
		self.semster =semster
		self.title = title
		self.link =link
		self.element =element
	def makeFolder(self):
		if not os.path.exists("testing/"+self.title):
    			os.mkdir("testing/"+self.title)
	




