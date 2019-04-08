import xml.etree.ElementTree as et

#生成student元素
stu = et.Element("Student1")
#生成子元素name，再student下面
name = et.SubElement(stu,"Name")
#name添加属性
name.attrib = {'lang','en'}
name.text = 'maoze'


age = et.SubElement(stu,'Age')
age.text = 18

et.dump(stu)