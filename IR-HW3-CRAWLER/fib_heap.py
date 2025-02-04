import time
from random import randint
from fibheap import *


heap1 = makefheap()
h = []
n = 100
r=100
a=fheappush(heap1,0.1)
b=fheappush(heap1,0.01)
hasg={}
hasg["u"]=a
k=hasg["u"]
k.key=-1
c=heap1.extract_min()
print(c.key)

# for i in range(0, n):
#     fheappush(heap1, (r-1,"abc"))
#     r-=1

# test fib heap running time
# heap1.decrease_key(a,0.001)
# heap1.decrease_key(b,0.002)
# print(a.key)
# c=heap1.extract_min()
# print(heap1.extract_min().key)
# kl=n

# start_time = time.time()
# while kl > 0:
#     m = heap1.extract_min()
#     print(m.key)
#     kl-=1
# print ("seconds run time for fib-heap-library", (time.time() - start_time))
# a=heap1.min
# heap1.decrease_key(a,-1)
# a=heap1.min
# print(a)
