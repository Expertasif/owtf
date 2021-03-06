#!/usr/bin/env python
'''
owtf is an OWASP+PTES-focused try to unite great tools and facilitate pen testing
Copyright (c) 2011, Abraham Aranguren <name.surname@gmail.com> Twitter: @7a_ http://7-a.org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;

The random module allows the rest of the framework to have access to random functionality
'''
from framework.lib.general import *
#from pyvirtualdisplay import Display
#from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest#, time, re

class URLLauncher(unittest.TestCase):
	def __init__(self, Selenium, BaseURL, VectorFile):
		self.Selenium = Selenium
		self.URLList = []
		for Vector in GetFileAsList(VectorFile):
			self.URLList.append(BaseURL + Vector)
	
	def Run(self):
		self.SetUp()
    		self.TestURLs()

	def SetUp(self):
		#self.Display = Display(visible=0, size=(800, 600))
		#self.Display.start()
		#self.Driver = webdriver.Firefox()
		#self.Driver.implicitly_wait(30)
		self.verificationErrors = []

	def TestURLs(self):
		for URL in self.URLList:
			cprint("Launching URL: "+URL)
			self.Selenium.Driver.get(URL)

	def is_element_present(self, how, what):
		try: self.Selenium.Driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True

	def is_element_present(self, how, what):
		try: self.Selenium.Driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True

	def tearDown(self):
		self.Selenium.Driver.quit()
		self.assertEqual([], self.verificationErrors)

