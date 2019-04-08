from lxml import etree
#只能读取xml文件
html = etree.parse("xml01.xml")

rst = etree.tostring(html,pretty_print=True)
print(rst)