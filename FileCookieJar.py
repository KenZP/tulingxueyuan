from urllib import request, error,parse
from http import cookiejar


filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

cookie_handler = request.HTTPCookieProcessor(cookie)

http_handler = request.HTTPHandler()

https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
	url = "http://www.renren.com/Plogin.do"

	data = {"emal":"13119144223","password":"123456"}

	data = parse.urlencode(data)

	req = request.Request(url,data=data.encode())

	rsp = opener.open(req)

	cookie.save(ignore_discard=True,ignore_expires=True)


if __name__ == '__main__':
	login()
	