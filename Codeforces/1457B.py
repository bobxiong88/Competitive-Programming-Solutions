import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = float('inf')
    for x in range(1,101):
        res = 0
        cnt = 0
        for i in range(n):
            if cnt:
                cnt-=1
            elif a[i]!=x:
                cnt = k-1
                res += 1
        ans = min(ans, res)
    print(ans)
