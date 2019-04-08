from selenium import webdriver
import time


#通过key模拟键盘
from selenium.webdriver.common.keys import Keys

#操作那个浏览器就对那个浏览器建立一个实例
#自动按照环境变量查找相应的浏览器
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

#如果浏览器没有在相应的环境变量中，需要指定浏览器位置


driver.get("http://www.baidu.com")

#通过函数查找titile标签

print("Title:{0}".format(driver.title))
