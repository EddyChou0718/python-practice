import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://tw.stock.yahoo.com/')
res.encoding = 'utf-8'
soup = bs(res.text, 'html.parser')
d = soup.select('#main-4-HotStock-Proxy .table-grid ul')

n = 1
for s in d:
  print(n, s.text)

  n += 1

# print(d)