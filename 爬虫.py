import time
from selenium import webdriver
from bs4 import BeautifulSoup

url='https://sale.jd.com/act/fjIiwRb7gcD.html'

browser=webdriver.Chrome()
browser.get(url)
prices=[]

# click an item button
python_button = browser.find_elements_by_xpath('//*[@id="26140795"]/div/div/div/div/ul/li[1]')[0]
python_button.click()


# find the price
price=browser.find_elements_by_xpath('python_button = browser.find_elements_by_xpath(/html/body/div[8]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]')
prices.append(price)
print(prices)

