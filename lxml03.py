from lxml import etree
#只能读取xml文件
xml = etree.parse("xml01.xml")
print(type(xml))
rst = xml.xpath('//book')
print(type(rst))
print(rst)
#xpath的意思是，查找带有category属性值为sport的book元素
rst = xml.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)
rst = xml.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)