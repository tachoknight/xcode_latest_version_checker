#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()
firefox.get('https://en.wikipedia.org/wiki/Xcode')

b = firefox.find_elements(By.CLASS_NAME, 'infobox-data')

print(b[2].text)

firefox.close()