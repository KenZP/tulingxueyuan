import xml.dom.minidom

#from xml.dom.minidom import parse

DOMTree = xml.dom.minidom.parse("03.xml")

doc = DOMTree.documentElement

for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("------Node:{0}------".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
        	if child.nodeName == "Name":
        		print("Name:{0}".format(child.childNodes[0].data))
        	if child.nodeName == "Mobile":
        		print("Mobile:{0}".format(child.childNodes[0].data))
        	if child.nodeName == "Age":
        		print("Age:{0}".format(child.childNodes[0].data))
        		if child.hasAttribute("detail"):
        			print("Age-detail:{0}".format(child.getAttribute("detail")))
