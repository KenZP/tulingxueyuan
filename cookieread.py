from urllib import request, error,parse
from http import cookiejar


filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)

cookie_handler = request.HTTPCookieProcessor(cookie)

http_handler = request.HTTPHandler()

https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler,https_handler,cookie_handler)

	

def GetHomePage():
		url = "http://www.renren.com/965187997/profile"	

		rsp = opener.open(url)

		html = rsp.read().decode()

		with open("rsp.html","w") as f:
			f.write(html)

if __name__ == '__main__':
	GetHomePage()
	