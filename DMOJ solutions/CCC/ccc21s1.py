import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans += (a[i]+a[i+1])*b[i]/2
print(ans)