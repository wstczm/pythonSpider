#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-23 13:45:24
# @Author  : james.zhang

from selenium import webdriver
from bs4 import BeautifulSoup
import os

githuburl = ["assets-cdn.github.com", "github.global.ssl.fastly.net"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chromedriver = "C:/Python27/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)

for url in githuburl:

    ips = {}
    i = 0

    while i < 10:
        driver.get("http://tool.chinaz.com/dns?type=1&host=%s&ip=" % url)
        bs = BeautifulSoup(driver.page_source, "lxml")

        items = bs.select("li.ReListCent.ReLists.bor-b1s.clearfix")
        for item in items:
            try:

                ip = item.select("div.w60-0.tl p")[0].get_text().split(' ')[0]
                time = item.select("div.w14-0 p")[0].get_text()

                if ip not in ips:
                    ips[ip] = [int(time)]
                else:
                    times = ips[ip]
                    times.append(int(time))
                    ips[ip] = times

            except Exception as e:
                pass

        i = i + 1

    minip = None
    mintime = None
    for i, ip in enumerate(ips):
        avgtime = sum(ips[ip]) / len(ips[ip])
        if i == 0 or avgtime < mintime:
            mintime = avgtime
            minip = ip
    print minip, url

driver.quit()
