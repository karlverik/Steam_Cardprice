import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import Get_Headers
import time
from requests.adapters import HTTPAdapter
import random

headers = Get_Headers.headers_steam()
cookies = Get_Headers.cookies_MARKET()


def Get_Gamelist(n):
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    linklist=[]
    IDlist = []
    for pagenum in range(1, n+1):
        try:
            r = s.get(
                'https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=10&category1=998&category2=29&specials=1&page=%d' % pagenum,
                headers=headers, cookies=cookies, timeout=15)

        except:
            print("连接失败")
            r = s.get(
                'https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=10&category1=998&category2=29&specials=1&page=%d' % pagenum,
                headers=headers, cookies=cookies, timeout=15)
        time.sleep(random.randint(3, 10))
        soup = BeautifulSoup(r.text, 'lxml')
        soups = soup.find_all(href=re.compile(r"https://store.steampowered.com/app/"), class_="search_result_row ds_collapse_flag")
        for i in soups:
            i = i.attrs
            i = i['href']
            link = re.search('https://store.steampowered.com/app/(\d*?)/',i).group()
            ID = re.search('https://store.steampowered.com/app/(\d*?)/(.*?)/', i).group(1)
            linklist.append(link)
            IDlist.append(ID)
        print('已完成'+str(pagenum)+'页,目前共'+str(len(linklist)))
    return linklist, IDlist


def Get_df(n):
    linklist,IDlist = Get_Gamelist(n)
    df = pd.DataFrame(list(zip(linklist, IDlist)),
               columns=['Link', 'ID'])
    return df


if __name__ == "__main__":
    n = 40
    path = 'pack.xlsx'
    df = Get_df(n)
    df.to_excel(path)