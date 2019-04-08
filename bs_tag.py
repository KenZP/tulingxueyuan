from urllib import request
from bs4 import BeautifulSoup


url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,'lxml')
#bs自动编码
content = soup.prettify()
#print(content)
print("==" * 12)
print("==" * 12)
print(soup.link)
print("==" * 12)
print(soup.link.name)
print("==" * 12)
print(soup.link.attrs['type'])
#soup.link.attrs['type'] = 'hahah'

print(soup.title)
print("==" * 12)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)

print(soup.name)
print(soup.attrs)


