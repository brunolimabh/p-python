from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pandas as pd
import time

#abrir o site
browser = wb.Chrome()
browser.get("https://bank-secure.atlassian.net/xpto")
time.sleep(100)

#logar no site
# browser.find_element(By.XPATH, '//*[@id="search"]').send_keys("teste")
# browser.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click
# browser.find_element_by_xpath('//*[@id="query-builder-test"]').send_keys("g")
# browser.find_element_by_xpath('//*[@id="password"]').send_keys("")
# browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/form/div/div[3]/div[2]/button').click()
