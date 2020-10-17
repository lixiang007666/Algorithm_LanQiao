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


#deque
#d=deque() append() appendleft() pop() popleft()
#Counter
nums=[1,1,2,3,4,5,5,6,6]
datas = Counter(nums)
print(datas)
print(datas[1])
print(datas[4])
for each in datas.keys():
    if datas[each] == 1:
        print(each)


