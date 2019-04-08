import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def getMsg():
	email = "1366798119@qq.com"
	pwd = "dhfjudhjfhfd"

	pop3_srv = "pop.qq.com" #端口995

	srv = poplib.POP3_SSL(pop3_srv)

	srv.user(email)
	srv.pass_(pwd)

	msgs, counts = srv.stat()
	print("Message:{0}, Size:{1}".format(msgs,counts))


	rsp,mails,octets = srv.list()
	print(mails)


	index = len(mails)

	rsp,lines,octets = srv.retr(index)


	msg_count = b'\r\n'.join(lines).decode("utf-8")

	msg = Parser().parsestr(msg_count)

	srv.quit()

	return msg



def parseMsg(msg,indent=0):
	if indent == 0:
		for header in ['From','To','Subject']:
			value = msg.get(header,'')
			if value:
				if header == 'Subject':
					value = decodeStr(value)
				else:
					hdr,addr = parseaddr(value)
					name = decodeStr(hdr)
					value = "{0}<{1}>".format(name,addr)
			print("{0},{1}:{2}".format(indent,header,value))

	if (msg.is_multipart()):
		parts = msg.get_payload()

		for n,part in enumerate(parts):
			print("{0} spart:{1}".format(''*indent,n))
			parseMsg(part,indent+1)
	else:
		content_type = msg.get_content_type()

		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode=True)
			charset = guessCharset(msg)
			if charset:
				content = content.decode(charset)
			print("{0}Text:{1}".format(indent,content))

		else:
			print("{0}Attachment:{1}".format(indent,content_type))


def decodeStr(s):
	value,charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)

	return value

def guessCharset(msg):
	charset = msg.get_charset()

	if charset is None:
		content_type = msg.get("Content-Type","").lower()
		pos = content_type.find("charset=")
		if pos >= 0:
			charset = content_type[pos+8:].strip()

	return charset


if __name__ == '__main__':
	msg = getMsg()
	print(msg)
	parseMsg(msg,0)