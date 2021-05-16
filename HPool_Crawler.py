import datetime
import logging
import time
from selenium import webdriver
import json
import re
from pathlib import Path
import pandas as pd
from glob import glob


def DailyAverage():
    """
    :param date: date formatted as yyyy-mm-dd-hh-mm
    """
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    today = glob(f'./{current_time}-*.csv')
    cache = []
    for file in today:
        cache.append(pd.read_csv(file))
    full = pd.concat(cache, join='outer', axis=0, ignore_index=True)
    full = full.drop('Unnamed: 0', axis=1)
    full = full.fillna(0)
    full = full.sum(axis=0) / full.shape[0]
    full = pd.DataFrame(full, columns=['Average']).T
    full.to_csv(str(Path.cwd() /  Path(f'{current_time}.csv')))
    return full


def Convert2Tera(raw):
    for miner in raw:
        if miner[2] == 'GB':
            miner[1] = str(round(float(miner[1]) / 1000, 2))
            miner[2] = 'TB'
    return raw


def SanityCheck(raw):
    cache = []
    for i, miner in enumerate(raw):
        if miner[-3] != u'在线':
            cache.append(i)
    for offlines in cache:
        raw.pop(int(offlines))
    return raw


def Convert2Dict(raw):
    kv = {}
    for miner in raw:
        kv[miner[0]] = miner[1]
    return kv


def toLowerCase(string):
    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in string)


def FormatString(raw):
    for miner in raw:
        miner[0] = miner[0].lower()
    return raw


def ParsebyJson(raw, save_dir):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    save_dir = Path(save_dir)
    with open('worker_keywords.json') as json_file:
        kv = json.load(json_file)
        for key in kv:
            for worker in raw:
                if re.search(key, worker):
                    kv[key].append(float(raw[worker]))
    for key in kv:
        kv[key] = sum(kv[key])
    keys = pd.DataFrame(data=raw, index=['volume'])
    keys.to_csv(str(save_dir / Path(f'{current_time}.csv')))


def main():
    logging.basicConfig(level=logging.NOTSET)

    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\tiwang\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r"profile-directory=Profile 1")
    driver = webdriver.Chrome(r'./chromedriver.exe', chrome_options=options)
    driver.get("https://www.hpool.com/center/machine")
    time.sleep(2)
    result = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/table/tbody').text
    driver.quit()

    result = result.splitlines()
    result = [x.split(' ') for x in result]
    result = Convert2Tera(result)
    result = SanityCheck(result)
    result = FormatString(result)
    result = Convert2Dict(result)

    ParsebyJson(result, './')


if __name__ == "__main__":
    main()
