import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
c = sum(a)//N
ans = 0
for i in a:
    if i!=c:
        ans += 1
print(ans)