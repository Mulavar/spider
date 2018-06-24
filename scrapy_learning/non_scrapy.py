# -*- coding:utf-8 -*-
import sys
import requests
import re



url_org = "http://quotes.toscrape.com/page/"

page = 1

# print(sys.getdefaultencoding())
while True:
    url = url_org + str(page)
    response = requests.get(url)
    # print(response.encoding)
    text = response.text
    # print(text)

    quote_pattern = '<span class="text" itemprop="text">“(.*?)”</span>'
    author_pattern = '<span>by <small class="author" itemprop="author">(.*?)</small>'
    keywords_pattern = '<meta class="keywords" itemprop="keywords" content="(.*?)" /    >'

    quote = re.findall(quote_pattern, text)
    author = re.findall(author_pattern, text)
    keywords = re.findall(keywords_pattern, text)

    quote_r = []
    for q in quote:
        q = re.sub(r"&#39;", r"'", q)
        quote_r.append(q)


    print(quote_r)
    print(author)
    print(keywords)

    if not re.findall("next", text):
        break


    page += 1