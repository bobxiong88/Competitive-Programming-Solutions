import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
has = [False]*N
for i in a:
    has[i-1] = True
if all(has):
    print("YES")
else:
    print("NO")