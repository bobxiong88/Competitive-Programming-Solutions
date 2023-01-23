import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
mx = -float('inf')
curr = 1
mp = defaultdict(lambda:0) 
dp = [0 for i in range(n)] 
mx = -sys.maxsize 
for i in range(n): 
    if a[i] - 1 in mp: 
        lastIndex = mp[a[i] - 1] - 1
        dp[i] = 1 + dp[lastIndex] 
    else: 
        dp[i] = 1
    mp[a[i]] = i + 1
    if dp[i]>mx:
        mx = dp[i]
        curr = a[i]
b = []
for i in range(-1,-n-1,-1):
    if a[i] == curr:
        b.append(n+i+1)
        curr-=1
print(mx)
print(*b[::-1])

    
