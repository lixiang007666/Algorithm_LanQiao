import math
import cmath
import sys
import string
import bisect
import heapq
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key
a = [[1,2], [2,4], [1,3]]
a.sort(key=lambda x: (x[0], -x[1]))
print(a)
