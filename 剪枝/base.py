import math
import cmath
import sys
import string
import bisect
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from itertools import combinations,permutations
from collections import Counter,deque
from functools import cmp_to_key

def dfs(num,part,now):#分别表示剩余待分的数，分的机会数和现在要选出的数。
    if part==1:
        return 1#出口
    #递归体
    sum1=0
    for i in range(now,num//part+1):#剪枝：不需要枚举到num，否则既有可能重复计算，又会加大运算量(dfs你懂的)。！！！！
        sum1+=dfs(num-i,part-1,i)#再搜索剩余待分数num-i，分的机会数少1，选择分出now，将所有情况统计于sum。
    return sum1

if __name__=="__main__":
    n,k=list(map(int,input().split()))
    res=dfs(n,k,1)
    print(res)


