"""
自定义进程类
"""
from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    def __init__(self,value):
        super().__init__()  # 调用Process类的init方法，获取父类中定义的属性
        self.value = value

    def fun1(self):
        sleep(2)
        print("复杂步骤1")
    def fun2(self):
        sleep(3)
        print("复杂步骤2")

    # 进程函数
    def run(self):
        self.fun1()
        self.fun2()


p = MyProcess(2)
p.start() # 自动运行run()
p.join()