# -*- coding: utf-8 -*-
import pymysql
from selenium import webdriver

# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
base_url = 'https://wwww.baidu.com'
driver.get(base_url)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()