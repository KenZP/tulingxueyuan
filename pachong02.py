import urllib
import chardet


if __name__ == '__main__':
	url = "https://www.cnblogs.com/zhaof/p/6910871.html"
	rsp = urllib.request.urlopen(url)
	print(type(rsp))
	print(rsp)

	print("URL:{0}".format(rsp.geturl()))
	print("INFO:{0}".format(rsp.info()))
	print("CODE:{0}".format(rsp.getcode()))
	html = rsp.read()
	cs = chardet.detect(html)
    print(type(cs))
    print(cs)

	html = html.decode(cs.get("encoding","utf-8"))
	print(html)