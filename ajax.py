"""
爬去豆瓣电影网
了解ajax的基本爬取方式

"""
from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=80&limit=20"


rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)