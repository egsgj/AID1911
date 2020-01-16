"""
使用进程池拷贝一个目录（包含目录中所有内容），目录中
包含若干个普通文件。

       *  目录中的每个文件拷贝过程都需要一个单独的进程去
       实现

       *  拷贝过程中实时显示拷贝的百分比


       os.mkdir() 创建目录
"""

from multiprocessing import Pool
import os

base_path = "/home/tarena/" # 要拷贝的目录在这个目录下
dir = input("要拷贝的目录：")
old_folder = base_path + dir

# 新的目录
new_folder = old_folder+'-备份'
os.mkdir(new_folder)

def copy_file(file):
    fr = open(old_folder+'/'+file,'rb')
    fw = open(new_folder+'/'+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


# 一共有哪些文件
all_files = os.listdir(old_folder)
# 使用进程池拷贝
pool = Pool()
for file in all_files:
    # 每copy一个文件就是一个事件
    pool.apply_async(copy_file,args=(file,))
pool.close()
pool.join()






