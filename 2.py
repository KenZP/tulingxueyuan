# 利用time函数生成两个函数
# 程序调用
# 计算总的执行时间

import time
import _thread as thread


def loop1():
    # ctime 得到当前时间
    print("start loop 1 at : ", time.ctime())
    time.sleep(4)
    print("end loop 1 at : ", time.ctime())


def loop2():
    print("start loop 2 at: ", time.ctime())
    time.sleep(2)
    print("end loop 2 at: ", time.ctime())


def main():
    print("starting at : ", time.ctime())
    # 参数两个：一个是需要运行的函数名，第二个是被运行函数的参数作为元组使用，被运行的函数参数为空则使用空元祖
    # 注意： 如果被运行的函数只有一个参数，需要参数后面加上逗号。
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("all done at: ", time.ctime())


if __name__ == '__main__':
    main()
    #while True:
     #   time.sleep(1)