import sys
input = sys.stdin.readline
from math import ceil
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    i = 0
    j = n*k-1
    ans = 0
    for _ in range(k):
        curr = []
        for x in range(ceil(n/2)-1):
            curr.append(a[i])
            i+=1
        rem = n-(ceil(n/2)-1)
        for x in range(j-rem+1,j+1):
            curr.append(a[x])
        j -= rem
        ans += curr[ceil(n/2)-1]
    print(ans)
