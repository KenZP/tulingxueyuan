#使用Urllib.request请求网页，并打印网页

from urllib import request,parse

if __name__ == '__main__':
	base_url = "https://www.baidu.com/s?"
	#wd = input("input your keyword")
	wd = "大熊猫"
	qs = {"wd":wd}

	qs = parse.urlencode(qs)
	print(qs)
	fullurl = base_url + qs
	print(fullurl) 
	rsp = request.urlopen(fullurl)

	html = rsp.read()
	html = html.decode("utf-8")
	print(html)