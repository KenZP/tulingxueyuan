#使用Urllib.request请求网页，并打印网页

from urllib import request

if __name__ == '__main__':
	url = "https://www.cnblogs.com/zhaof/p/6910871.html"
	rsp = request.urlopen(url)
	html = rsp.read()
	html = html.decode("utf-8")
	print(html)