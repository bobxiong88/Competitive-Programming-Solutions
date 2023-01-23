import sys
from math import ceil
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    i = n-1
    c = 0
    a = [0]+[i for i in range(1,n+1)]
    out = []
    while True:
        if ceil(n**0.5) == i:
            out.append((n, i))
            out.append((n, i))
            a[n] = ceil(a[n]/a[i])
            a[n] = ceil(a[n]/a[i])
            n = i
            i = n-1
        else:
            out.append((i,n))
            a[i] = ceil(a[i]/a[n])
            i -=1
        if i == 1:
            break
    print(len(out))
    for i in out:
        print(*i)
        
    
