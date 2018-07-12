import requests
from bs4 import BeautifulSoup
import json

url = 'http://nesa.zju.edu.cn/webpage/people.html'
response = requests.get(url)

soup = BeautifulSoup(str(response.content, 'utf8'))

people_list = soup.select('div[class="view view-ninth"]')
# print(people)

name_list = []
position_list = []

for people in people_list:
    name = people.find('h2').get_text()
    # print(name)
    position = people.find('p').get_text()
    name_list.append(name)
    position_list.append(position)


f = open('nesa.json', 'w')
dit = dict(zip(name_list, position_list))
content = json.dumps(dit, ensure_ascii=False)
f.write(content)
f.close()
# print(f.read())
f1 = open('nesa.json', 'r')
data = json.load(f1)
print('data:', data)
f1.close()