from urllib import request, error,parse
from http import cookiejar


cookie = cookiejar.CookieJar()

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

def GetHomePage():
		url = "http://www.renren.com/965187997/profile"	

		rsp = opener.open(url)

		html = rsp.read().decode()

		with open("cookie.html","w") as f:
			f.write(html)

if __name__ == '__main__':
	login()
	GetHomePage()