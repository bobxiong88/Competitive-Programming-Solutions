import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int,input().split()))
    prefix = []
    suffix = []
    s = -1
    c = 0
    index = float('inf')
    sor = sorted(a)
    if sor == a:
        print(0)
        continue
    elif sor == a[::-1]:
        print(0)
        continue
    for i in range(1,k):
        prefix.append(a[i]-a[i-1])
    s = 0
    for i in range(-2,-k-1,-1):
        suffix.append(a[i]-a[i+1])
    suffix = suffix[::-1]
    switch = False
    ans = 0
    for i in range(-1,-k,-1):
        if suffix[i]>=0 and switch == False:
            ans+=1
            continue
        else:
            switch = True
        if switch and suffix[i]<=0:
            ans+=1
        else:
            break
    print(k-ans-1)
    
