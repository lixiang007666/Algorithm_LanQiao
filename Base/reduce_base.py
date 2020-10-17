import math
import cmath
import sys
import string
import heapq
import bisect
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key,reduce

def fun(x,y):
    return x*y

a=reduce(fun,[1,2,3])
print(a)

#每组有gcd张牌。
from functools import reduce
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a % b)
        return reduce(gcd, Counter(deck).values()) > 1


#4 8  每组4张都相等
#2 8 4 每组两张都相等
#3 4   False

