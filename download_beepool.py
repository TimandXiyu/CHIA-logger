import requests
import datetime
import logging
import os
import time
from bs4 import BeautifulSoup as bs
from xls_parser import to_easy_csv
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.NOTSET)

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\Tim Wang\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"profile-directory=Profile 1")
driver = webdriver.Chrome(r'./chromedriver.exe', chrome_options=options)

driver.get("https://www.hpool.com/center/machine")

time.sleep(2)
result = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/table/tbody/tr').text
print(result)














def get_xls():
    url = 'https://www.hpool.com/center/machine'
    cookie = {'auth_token': 'eyJldCI6MTYyMjMwMDQ3NiwiZ2lkIjo2NCwidWlkIjoxNzQ5MTA0fQ==.R56BNMCSXIgGIdci+FU0oHY3jFcNtm6JlpWQutY56qIP3zAdjislOfsnsyAbaCvTR4SnIXh4LYPBvJhqzFwgxZMpqYz4L2bPFhaSg56PhJ2op4aC4fTgVjbkUUj99IyZj/vRKwtWvzCAvQsz8yRDt3Bqx4rGbEvYR+jpvqxPAdKpnfb49gD9XE9aKbsUbt9zClKoVq+s8w6Sqy8kuq/a5j+PZJBpZRT0cMhF8TIdH6ZPzUuWShd74sxAfvh1rryG4XS9qFSm+MTErfEyEeZxmVlXD/qoTFlWkrizOR/DOtb8ECQbbemzxek1EyftxVO0w8f0BZLS67eFJq94bEEuQA==',
              'MEIQIA_TRACK_ID': '1sZqCVPcNUfYGdbu6aG5BuWLzqZ',
              '_gid': 'GA1.2.778293166.1621090329',
              '_ga': 'GA1.2.1236701797.1621090329',
              'lang': 'zh'}


    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',}


    res = requests.get(url=url, headers=headers, cookies=cookie).content.decode("utf-8")
    soup = bs(res, 'html')
    b = soup.find_all('ant-spin-container')
    print(b)
    with open("hpool.html", "w", encoding="utf-8") as f:
        f.write(res)

if __name__ == '__main__':
    get_xls()


