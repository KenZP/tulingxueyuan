#分析百度词典
from urllib import request,parse
import json

if __name__ == '__main__':
	base_url = "https://fanyi.baidu.com/sug"
	wd = input("input your keyword:")
	data = {'kw':wd}
	data = parse.urlencode(data).encode('utf-8')
	#print(type(data))

	#headers = {'Content-Length':len(data)}
	rsp = request.urlopen(base_url,data=data)

	json_data = rsp.read().decode('utf-8')
	json_data = json.loads(json_data)
	#print(json_data)

	for item in json_data['data']:
		print(item['k'],"---",item['v'])