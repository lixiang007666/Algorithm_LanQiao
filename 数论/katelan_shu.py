import math
import cmath
import sys
import string
import heapq
import bisect
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key

if __name__=="__main__":
    n=int(input())
    f=[0 for i in range(20)]
    f[0]=1
    f[1]=1
    for i in range(2,n+1):
        for j in range(0,i):
            f[i]+=f[j]*f[i-1-j]
    print(f[n])