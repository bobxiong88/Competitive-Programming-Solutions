import sys
input = sys.stdin.readline
N, K = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
a.sort(reverse = True)
for i in range(K):
    ans += a[i]
print(ans)