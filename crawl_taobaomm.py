# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
input = browser.find_element_by_id("kw")
input.send_keys(u"宋倩倩")

time.sleep(2)

submit = browser.find_element_by_id("su")
submit.click()
