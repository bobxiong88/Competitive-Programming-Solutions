import sys
input = sys.stdin.readline
q = int(input())
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
if q == 1:
    b.sort()
else:
    b.sort(reverse = True)
ans = 0
for i in range(n):
    ans += max(a[i],b[i])
print(ans)