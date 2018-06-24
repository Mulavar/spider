import requests
import re
from bs4 import BeautifulSoup
import pymysql

url_org = "https://movie.douban.com/top250?start="
# print(requests.get(url_st).text)
start = 0



while True:
    url = url_org + str(start)
    response = requests.get(url)
    soup = response.text
    # print(soup)

    # 获取标题
    title_list = re.findall('<span class="title">([^a-z]*?)\s*?</span>', str(soup), re.S)
    print(len(title_list))
    print(title_list)

    # 获取导演
    director_list = re.findall('<p class="">\s*?导演: (\S*)', str(soup), re.S)
    print(director_list)

    # 获取年份
    year_list = re.findall('<div class="bd">\s*?<p class="">.*?(\d{4})', str(soup), re.S)
    print(year_list)

    # 获取评分
    rating_list = re.findall('<span class="rating_num" property="v:average">(.*?)</span>', str(soup))
    print(rating_list)

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='qwer1234',
                                 use_unicode=True,
                                 charset='utf8mb4')
    # try:
    #     with connection.cursor() as c:
    #         sql1 = 'use spider;'
    #         c.execute(sql1)
    #         for i in range(25):
    #             sql2 = 'insert into douban_film(`title`, `director`, `year`, `rating`) values(%s, %s, %s, %s)'
    #             c.execute(sql2, (title_list[i], director_list[i], year_list[i], rating_list[i]))
    #             connection.commit()
    # finally:
    #     connection.close()

    next_page = BeautifulSoup(soup).find_all(attrs={"class": "next"})
    start += 25
    if not re.search("link", str(next_page[0])):
        break








