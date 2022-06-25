import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import Get_Headers
import time
import random
from requests.adapters import HTTPAdapter

headers = Get_Headers.headers_steam()
cookies = Get_Headers.cookies_MARKET()


def gamename(soup):   #游戏名字
    try:
        a = soup.find('h1')
        k = str(a.string)
    except:
        a = soup.find('h1')
        k = str(a.text)
    k = re.sub('Buy', '',  k)
    k = re.sub('Download', '', k)
    k = re.sub('Demo', '', k)
    return k.strip()


def gameprice(soup):#价格
    global temp_price
    try:
        a = soup.findAll(class_="discount_final_price")
        for i in a:
            if re.search('¥|free|免费', str(i), re.IGNORECASE):
                a = i
        k = re.search(">.*?<", str(a[0])).group()[1:-1].strip()
    except:
        try:
            a = soup.findAll(class_="game_purchase_price price")
            for i in a:
                if re.search('¥|free|免费', str(i), re.IGNORECASE):
                    a = i
            k = re.search(">.*?<", str(a[0])).group()[1:-2].strip()
        except:
            k = str(temp_price)
    temp_price = k
    return k


def packprice(x, tx, s): #补充包价格获取
    global c2
    u = 'https://steamcommunity.com/market/listings/753/'
    link = 'https://steamcommunity.com/market/search?q=&category_753_Game[]=tag_app_' + str(x['ID']) + '&category_753_item_class%5B%5D=tag_item_class_5&appid=753'
    print(str(link))
    try:
        r = s.get(link, headers=headers, cookies=cookies, timeout=15)
    except:
        print('服务器无响应1')
    try:
        t = r.text
        data_hash_name = u + re.search('data-hash-name="(.*?)"', t).group(1)
        price = re.search('currency="\d+">(.*?)<', t).group(1)
        print(data_hash_name)
        print(price)
    except:
        print('市场访问错误，等待10秒重新尝试连接')
        time.sleep(10)
        try:
            r = s.get(link, headers=headers, cookies=cookies, timeout=15)
        except:
            print('服务器无响应2')
        try:
            t = r.text
            data_hash_name = u + re.search('data-hash-name="(.*?)"', t).group(1)
            price = re.search('currency="\d+">(.*?)<', t).group(1)
            print(data_hash_name)
            print(price)
        except:
            price = None
            data_hash_name = None
    time.sleep(random.randint(3, 10))

    tx.at[tx.index[c2], '补充包价格'] = price
    tx.at[tx.index[c2], '补充包链接'] = data_hash_name
    tx.to_excel('pack.xlsx', index=False)
    c2 += 1
    print('已经获取第' + str(c2) + '个补充包信息')
    return price, data_hash_name


def getdetail(x, tx, s):
    global c1
    price, name = ' ', ' '
    print(x['Link'])
    try:
        r = s.get(x['Link'], headers=headers, cookies=cookies, timeout=15)
    except:
        print('服务器无响应1')

    soup = BeautifulSoup(r.text, 'lxml')
    try:
        name = gamename(soup)
        price = gameprice(soup)
        print(name, price)
    except:
        name = x['ID']
        price = None
    time.sleep(random.randint(3, 10))
    tx.at[tx.index[c1], '名字'] = name
    tx.at[tx.index[c1], '价格'] = price
    tx.to_excel('pack.xlsx', index=False)
    c1 += 1
    print('已经搜索第' + str(c1) + '个游戏')
    return name, price


def main(c):
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    df = pd.read_excel('pack.xlsx')
    df[c:].apply(lambda x: getdetail(x, df, s), axis=1)
    print('已完成全部')


def fill(c):
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    df = pd.read_excel('pack.xlsx')
    df[c:].apply(lambda x: packprice(x, df, s), axis=1)
    print('已完成全部')


if __name__ == "__main__":
    c1 = 789
    c2 = 866
    #main(c1)
    fill(c2)


