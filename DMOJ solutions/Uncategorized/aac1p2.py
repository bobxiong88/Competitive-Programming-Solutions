import sys
input = sys.stdin.readline
from math import floor
N, D, K, X = map(int,input().split())
a = [int(input()) for i in range(N)]
P = int(input())
a.sort(reverse = True)
win = True
for i in range(N):
    while K and a[i] >= P:
        a[i] = floor(a[i]*(100-X)/100)
        K-=1
    if a[i] >= P:
        win = False
print("YES" if win else "NO")