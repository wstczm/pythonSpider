# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://fgowiki.com/guide")

driver.maximize_window()

elem = driver.find_element_by_css_selector("input.form-control.guanjian")
elem.send_keys(u"冲")
time.sleep(1)
elem.send_keys(u"田")

time.sleep(2)

links = driver.find_element_by_css_selector('div.data.pull-left a')
links.click()

time.sleep(2)

target = driver.find_element_by_css_selector("li.swiper-slide.Card.swiper-slide-active")
driver.execute_script("arguments[0].scrollIntoView();", target)

time.sleep(2)

next = driver.find_element_by_css_selector('div.swiper-button-next')
next.click()

time.sleep(1)

next = driver.find_element_by_css_selector('div.swiper-button-next')
next.click()

time.sleep(1)

next = driver.find_element_by_css_selector('div.swiper-button-next')
next.click()

time.sleep(2)

45880
