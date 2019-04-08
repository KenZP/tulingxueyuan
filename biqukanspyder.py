# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

# BaseUrl = "https://www.biqukan.com/1_1094"
# url = "https://www.biqukan.com/1_1094/5403177.html"

# req = requests.get(url)
# #print(req.text)

# html = req.text
# bf = BeautifulSoup(html,features="lxml")

# texts = bf.find_all('div',class_ = 'showtxt')

# #print(texts)

# txt = texts[0].text.replace('\xa0'*8,'\n\n')
# print(txt)


class DownLoadXiSh(object):
	"""docstring for DownLoadXiSh"""
	def __init__(self):
		#super(DownLoadXiSh, self).__init__()
		self.server = "https://www.biqukan.com"
		self.url = "https://www.biqukan.com/1_1094"
		self.urls = []
		self.names = []
		self.nums = 0
		

	def GetUrlsAndTitles(self):
		# server = "https://www.biqukan.com"
		# url = "https://www.biqukan.com/1_1094"
		# urls = []
		# names = []
		# nums = 0
		req = requests.get(self.url)
		html = req.text
		div_bf = BeautifulSoup(html,features="lxml")
		div = div_bf.find_all('div',class_ = 'listmain')
		#print(div[0])

		a_bf = BeautifulSoup(str(div[0]),features="lxml")
		a = a_bf.find_all('a')
		#print(a)

		for each in a[16:-1]:
			self.urls.append(self.server + each.get('href'))
			self.names.append(each.string)
			#print(each.string, server + each.get('href'))
		# for url in urls:
		# 	print(url)

		# for name in names:
		# 	print(name)
		self.nums = len(self.urls)

		#return urls, names, nums


	def get_contents(self,url):
		req = requests.get(url)
		html = req.text
		bf = BeautifulSoup(html, features="lxml")
		texts = bf.find_all('div',class_ = 'showtxt')
		#texts = texts[0].text.replace('\xa0'*8,'\n\n')
		texts = texts[0].text
		return texts


	def WriteToFile(self,file,name):
		with open(name + '.txt','w',encoding='utf-8') as f:
			f.write(file)

	def WriteToFile1(self,file,name,path):
		with open(path,'a',encoding='utf-8') as f:
			f.write(name +'\n')
			f.write(file)
			f.write('\n\n')

	def download(self,urls,titles,nums):
		for i in range(nums):
			texts = self.get_contents(urls[i])
			self.WriteToFile(texts,titles[i])

if __name__ == '__main__':

	dl = DownLoadXiSh()

	dl.GetUrlsAndTitles()

	# for url in dl.urls:
	#  	print(url)

	# for name in dl.names:
	# 	print(name)

	# print(titles[0])

	#def download(self,urls,titles,nums):
	print("开始下载：")
	for i in range(dl.nums):
		texts = dl.get_contents(dl.urls[i])
		dl.WriteToFile(texts,dl.names[i])
		#dl.WriteToFile1(texts,dl.names[i],'yiye.txt')
		sys.stdout.write("已下载：%.3f%%"%float(i/dl.nums) + '\r')
		sys.stdout.flush()
	print("下载完成")	

	#dl.download(dl.urls,dl.names,dl.nums)


