import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = tuple(map(int,input().split()))
    diffs = []
    for i in a:
        if not i%k==0:
            diffs.append(k-i%k)
    diffs.sort()
    if not diffs:
        print(0)
        continue
    d = {}
    c = 0
    diff = 0
    for i in diffs:
        try:
            d[i]+=1
        except:
            d.update({i:1})
        if d[i]>c:
            c = d[i]
            diff = i
        elif d[i]==c:
            diff = max(diff, i)
    print(k*(c-1)+diff+1)
