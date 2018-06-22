import re
import requests
from bs4 import BeautifulSoup

string = "abcdabcd"
pattern = "(\w*?)d"
print(re.findall(pattern, string))


s1 = '''
    <span class="title">荒岛余生</span>
                                    <span class="title">&nbsp;/&nbsp;Cast Away</span>
                                <span class="other">&nbsp;/&nbsp;浩劫重生(台)  /  劫后重生(港)</span>
'''

r1 = re.findall('<span class="title">(.*?)</span>.*?<span class="title">', s1, re.S)
print(r1)


s2 = "主演"
p2 = "\w"
print(re.search(p2, s2))


s3 = '<span class="rating_num" property="v:average">9.4</span>'
p3 = '<span class="rating_num" property="v:average">(.*?)</span>'
print(re.findall(p3, s3))

url_org = "https://movie.douban.com/top250?start="
s4 = requests.get(url_org+"0").text
s4 = BeautifulSoup(s4)
print(str(s4))
print(s4.decode('utf-8'))
print(re.findall(p3, str(s4)))



num = '10.5'
print(float(num))