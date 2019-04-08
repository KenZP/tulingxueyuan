from urllib import request
from bs4 import BeautifulSoup
import re

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,'lxml')
#bs自动编码
content = soup.prettify()
#print(content)

#print(soup.name)


print("==" * 12)
tags = soup.find_all(re.compile('^me'),content="always")
for tag in tags:
	print(tag)
print(tags)
print("==" * 12)