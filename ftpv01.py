import ftplib
import os


HOST = "ftp.acc.umu.se"
DIR = 'Public/EFLIB'
FILE = 'README'

try:
	f = ftplib.FTP()
	f.set_debuglevel(2)
	f.connect(HOST)
except Exception as e:
	print(e)
	exit()
print("**CONNECT TO HOST {0}".format(HOST))



try:
	f.login()
except Exception as e:
	print(e)
	exit()
print("***Logged in as 'anonvmous'")





try:
	f.cwd(DIR)
except Exception as e:
	print(e)
	exit()
print("***Changed dir to {0}".format(DIR))


try:
	f.retrbinary('RETR {0}'.format(FILE), open(FILE,'wb').write)
except Exception as e:
	print(e)
	exit()


f.quit()