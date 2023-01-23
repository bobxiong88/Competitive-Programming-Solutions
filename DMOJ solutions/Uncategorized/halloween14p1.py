import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
if n>=k:
    d = n//k
    ans = min(n-d*k,(d+1)*k-n)
else:
    ans = k-n
print(ans)