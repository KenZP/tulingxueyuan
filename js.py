from urllib import request, parse


def youdao(key):
	url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

	data = {
		"i": "girl",
		"from": "AUTO",
		"to": "AUTO",
		"smartresult": "dict",
		"client": "fanyideskweb",
		"salt": "15541129882211",
		"sign": "a33b6f7bfbf04570efd582cf1e9707d9",
		"ts": "1554112988221",
		"bv": "33a62fdcf6913d2da91495dad54778d1",
		"doctype": "json",
		"version": "2.1",
		"keyfrom": "fanyi.web",
		"action": "FY_BY_REALTlME",
		"typoResult": "False"
	}

	data = parse.urlencode(data).encode()

	headers = {}

	req = request.Request(url,data=data)

	rsp = request.urlopen(req)

	html = rsp.read().decode()

	print(html)


if __name__ == '__main__':
	youdao("girl")
