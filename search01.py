import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one12two34threefour56")
print(m.group())


m = pattern.search("one12two34threefour56",10,40)
print(m.group())