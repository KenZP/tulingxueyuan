import requests
import json
from urllib import parse
if __name__ == '__main__':
	base_url = "https://fanyi.baidu.com/sug"
	#wd = input("input your keyword:")
	wd = 'girl'
	data = {'kw':wd}
	print(type(data))
	#因为使用post，至少因该包含Content-Length字段
	headers = {'Content-Length':str(len(data))}

	rsp = requests.post(url=base_url,data=data,headers=headers)
	print(rsp.text)
	print(rsp.json())