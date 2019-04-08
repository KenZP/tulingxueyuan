'''
Server端流程：
        1. 建立socket，socket是负责具体通信的一个实例
        2. 绑定，为创建的socket指派固定的端口和ip地址
        3. 接受对方发送内容
        4. 给对方发送反馈，此步骤为非必须步骤

'''

import socket

def serverFunc():


	#socket.AF_INET ipv4
	#socket.SOCK_DGRAM 使用UDP
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#127.0.0.1 这个ip地址代表机器本身
	#7852 随手指定的端口
	# 地址是一个tuple类型，（ip，port）
	addr = ("127.0.0.1",7852)
	sock.bind(addr)

	#recvfrom接受的返回值是一个元祖，前一项表示数据，后一项表示客户端地址
    #接受消息是死等
	#rst = sock.recvfrom(500)
	data,addr = sock.recvfrom(500)

	print(data)
	print(type(data))
    #接受的消息是Byte格式，需要解码为str
	text = data.decode()

	print(type(text))
	print(text)


	rsp = "Ich Hab Kenie Hunge"
    #发送的消息是Byte格式，需要编码
	data = rsp.encode()
	sock.sendto(data,addr)


	if __name__ == '__main__':
		print("server starting......")
		serverFunc()
		print("Server stopping......")
