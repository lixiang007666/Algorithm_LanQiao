import math
import cmath
import string
import sys
import bisect
import heapq
from queue import Queue, LifoQueue, PriorityQueue
from itertools import permutations, combinations
from collections import deque, Counter
from functools import cmp_to_key

g = [[0 for _ in range(55)] for _ in range(55)]
f = [[[0 for _ in range(34)] for _ in range(55)] for _ in range(55)]
n = 0


def pre():
    for p in range(1, 33):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if f[i][k][p - 1] and f[k][j][p - 1]:
                        f[i][j][p] = 1
                        g[i][j] = 1


def floyed():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and j != k and i != k:
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    print(n)
    print(g[1][n])


if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    for i in range(m):
        u, v = list(map(int, input().strip().split()))
        g[u][v] = 1
        f[u][v][0] = 1
    pre()
    floyed()


