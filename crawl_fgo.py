#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-25 10:41:45
# @Author  : james.zhang

from selenium import webdriver
from bs4 import BeautifulSoup
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chromedriver = "C:/Python27/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)

url = "https://fgowiki.com/guide/petdetail/189"

driver.get(url)
bs = BeautifulSoup(driver.page_source, "lxml")


print bs.select("div.textsmall.NAME")[0].get_text()
