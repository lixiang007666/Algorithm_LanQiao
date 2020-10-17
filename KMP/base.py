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

def Gen_next(str):
    i=0
    j=-1
    next=[-1]
    while i<(len(str)-1):
        if j==-1 or str[i]==str[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    print(next)
    return next

def kmp(s1,s2,pos=0):
    next=Gen_next(s2)
    i=pos
    j=0
    while i<len(s1) and j<len(s2):
        if j==-1 or s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            j=next[j]
    if j>=len(s2):
        return i-len(s2)
    else:
        return 0

if __name__=="__main__":
    s1 = "acabaabaabcacaabc"
    s2 = "abaabcac"
    print(kmp(s1, s2))




