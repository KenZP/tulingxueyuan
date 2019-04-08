'''
步骤
1.compile函数将正则表达式的字符串实例化为一个pattern对象
2.通过pattern对象的一些方法对文本进行匹配，匹配结果是一个Match对象
3.用Match对象的方法，对结果进行操作
'''

import re

#\d表示一个数字
#后面+号表示这个数字剋出现一次或者多次

s = r'\d+'  #r表示后面是字符串。不需要转义


pattern = re.compile(s)

m = pattern.match("one12two2three3")

print(type(m))
print(m)

#match参数,后面表示从哪里开始找，到哪里结束
m = pattern.match("one12two2three3",3,10)

print(type(m))
print(m.group())

print(m.start(0))
print(m.end(0))
print(m.span(0))
