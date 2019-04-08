import re

s = r'\d+'

pattern = re.compile(s)

s = pattern.findall("i am 18 years old and 185 high")
print(s)


s = pattern.finditer("i am 18 years old and 185 high")
print(type(s))

for i in s:
	print(i.group())
