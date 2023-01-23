import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,n+1):
        ans += i*(n-i+1)
    for i in range(n):
        if a[i] == 0:
            ans += (i+1)*(n-i)
    print(ans)
