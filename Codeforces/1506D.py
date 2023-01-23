import sys
input = sys.stdin.readline
from heapq import *
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    freq = dict()
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    arr = []
    for i in freq:
        arr.append(-freq[i])
    heapify(arr)
    while len(arr) > 1:
        a = -heappop(arr)
        b = -heappop(arr)
        a -= 1
        b -= 1
        
        if a:heappush(arr,-a)
        if b:heappush(arr,-b)
    if len(arr):
        print(-sum(arr))
    else:
        print(0)
