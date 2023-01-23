import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    ans= 0
    for i in range(n-1):
        v = max(a[i], a[i+1])/min(a[i], a[i+1])
        x = 2
        while x < v:
            x*=2
            ans += 1
    print(ans)
