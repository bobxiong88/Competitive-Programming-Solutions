import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    mn = float('inf')
    for i in range(n-1):
        mn = min(mn, a[i+1]-a[i])
    print(mn)
