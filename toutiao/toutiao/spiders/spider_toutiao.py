import scrapy
import time

import requests
from selenium import webdriver


def refresh_html(jianshu_url):
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    browser.get(jianshu_url)
    while True:
        time.sleep(1)
        browser.refresh()

refresh_html('https://www.wukong.com/answer/6724543173265195272/')