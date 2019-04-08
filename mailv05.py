from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart("alternative")

mail_content = """
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Title</title>
		</head>

		<body>
		<h1>这是一封HTML格式的邮件</h1>
		</body>
		</html>
		"""


msg_html = MIMEText(mail_content,"html","utf-8")

msg.attach(msg_html)

msg_text = MIMEText("I LOVE YOU","plain","utf-8")
msg.attach(msg_text)



from_addr = "1366798119@qq.com"
from_pwd = "hjpovygcxmrshhcj"

to_addr = "1366798119@qq.com"


smtp_srv = "smtp.qq.com"


try:
	import smtplib

	srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)

	srv.login(from_addr,from_pwd)
	srv.sendmail(from_addr,[to_addr],msg.as_string())
	srv.quit()
except Exception as e:
	print(e)
