import re
import requests

url = "https://www.zhihu.com/question/20852004"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
proxies = {
    'http': 'http://36.81.185.223:80',
}

requests.adapters.DEFAULT_RETRIES = 5

response1 = requests.get(url=url, headers=headers, proxies=proxies)
response2 = requests.get(url=url, headers=headers)

f1 = open('./data/d_proxies.html', 'wb')
f1.write(response1.content)
f1.close()



f2 = open('./data/d_non_proxies.html', 'wb')
f2.write(response2.content)
f2.close()
