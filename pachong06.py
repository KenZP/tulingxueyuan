#分析百度词典
from urllib import request,parse
import json

if __name__ == '__main__':
	base_url = "https://fanyi.baidu.com/sug"
	#wd = input("input your keyword:")
	wd = 'girl'
	data = {'kw':wd}
	data = parse.urlencode(data).encode('utf-8')
	#print(type(data))

	headers = {'Content-Length':len(data)}

	req = request.Request(url=base_url,data=data,headers=headers)
	#因为已经构造了一个request的请求对象，可以直接使用
	rsp = request.urlopen(req)

	json_data = rsp.read().decode('utf-8')
	json_data = json.loads(json_data)
	#print(json_data)

	for item in json_data['data']:
		print(item['k'],"---",item['v'])