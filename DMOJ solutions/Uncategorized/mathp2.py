import sys
input = sys.stdin.readline
m = int(1e9)+7
N = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += i*pow(2,N-1,m)
    ans %= m
print(ans)