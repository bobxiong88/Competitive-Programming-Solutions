import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if sum(a)/n in a: print("YES")
    else: print("NO")
