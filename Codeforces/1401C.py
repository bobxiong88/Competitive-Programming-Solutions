import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = sorted(a)
    m = min(a)
    b = [a[i] for i in range(n) if not a[i]%m]
    b.sort()
    b = deque(b)
    for i in range(n):
        if a[i]%m==0:
            a[i] = b.popleft()
    print("YES" if a==c else "NO")
