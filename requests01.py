import requests


url = "http://www.baidu.com"


rsp = requests.get(url)

print(rsp.text)


rsp = requests.request("get",url)

print(rsp.text)