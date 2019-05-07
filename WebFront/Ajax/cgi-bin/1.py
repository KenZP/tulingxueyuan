import cgi,cgitb,json,time
cgitb.enable()

print("Content-Type: text/html")  #html is following
print()                           # black line  end of headers


#接受用户发送的数据
fs = cgi.FieldStorage()
inputs = {}
for key in fs.keys():
    inputs[key] = fs[key].value

#给用户返回数据
#print(inputs)


#转换成json格式
print(json.dumps(inputs))