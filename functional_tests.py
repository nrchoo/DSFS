# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:33:45 2015

@author: nathanchoo
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title