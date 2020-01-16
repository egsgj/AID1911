# 求100000以内所有质数之和

import time
from multiprocessing import Process

def timeit(f):
    def wrapper(*args,**kwargs):
        s_t = time.time()
        res = f(*args,**kwargs)
        e_t = time.time()
        print("函数执行时间：%.6f"%(e_t-s_t))
        return res
    return wrapper

# 判断一个数是不是质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# 求和
@timeit
def prime():
    l = []
    for i in range(1,100001):
        if is_prime(i):
            l.append(i)
    return sum(l)

# prime() # 函数执行时间：26.753193

class Prime(Process):
    def __init__(self,pr,begin,end):
        super().__init__()
        self.pr = pr
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin,self.end):
            if is_prime(i):
                self.pr.append(i)
        print(sum(self.pr))

@timeit
def process_4():
    prime = []
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(prime,i,i+25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

# process_4() #函数执行时间：15.282414

@timeit
def process_10():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

process_10() # 函数执行时间：14.053634



