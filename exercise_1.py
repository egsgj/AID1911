"""
大文件拆分

       使用Process完成，要求将大文件拆分成2个小文件，
       按照字节大小去分成两个。要求上下两个部分同时操作。

       提示： 两个子进程分别去做
             注意读写偏移量控制
"""
from multiprocessing import Process
import os

filename = "timg.jpeg"
size = os.path.getsize(filename)

"""
对于IO操作来说，如果在父进程创建IO，进程从父进程获取了IO.
那么这些进程对该IO的操作可能相互有影响。
如果在各自进程中分别打开的IO相互没有任何影响 
"""
# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size // 2
    while True:
        if n <= 1024:
            data = fr.read(n)
            fw.write(data)
            break
        data = fr.read(1024)
        fw.write(data)
        n -= 1024
    fr.close()
    fw.close()

def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p1.start()
p2.start()

p1.join()
p2.join()







