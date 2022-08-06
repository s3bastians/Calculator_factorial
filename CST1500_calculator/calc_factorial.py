import threading
import math

class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        global result
        temp = math.factorial(self.num)
        print("%s: calculate %d's factorial is %d" %(self.name,self.num,temp))
        result += temp

result = 0
threads = []

def test():
    for i in range(1,6):
        t = f(i)
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()

if __name__ == '__main__':
    test()

    print('The result is %d' %result)