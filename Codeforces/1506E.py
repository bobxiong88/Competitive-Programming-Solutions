import sys
input = sys.stdin.readline
from heapq import *
from collections import deque
for _ in range(int(input())):
    n = int(input())
    q = list(map(int,input().split()))
    q.append(n+1)
    meme = [i for i in range(n,0,-1)]
    mn = []
    pog = deque([])
    last = 0
    used = set()
    for i in range(n+1):
        if q[i] != q[i-1]:
            used.add(q[i])
            while meme and meme[-1] <= q[i-1] and i != 0:
                k = meme.pop()
                if k not in used: pog.append(k)
            for j in range(i-last-1):
                mn.append(pog.popleft())
            mn.append(q[i])
            last = i
    print(*mn[:n])
    meme = [i for i in range(n,0,-1)]
    mx = []
    pog = deque([])
    last = 0
    used = set()
    for i in range(n+1):
        if q[i] != q[i-1]:
            used.add(q[i])
            while meme and meme[-1] <= q[i-1] and i != 0:
                k = meme.pop()
                if k not in used: pog.append(k)
            for j in range(i-last-1):
                mx.append(pog.pop())
            mx.append(q[i])
            last = i
    print(*mx[:n])
