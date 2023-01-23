import sys
input = sys.stdin.readline
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
if max(a)<=sum(a)-max(a) and sum(a)%2==0:
    print("YES")
else:
    print("NO")