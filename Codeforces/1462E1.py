import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    f1 = [0 for i in range(n+5)]
    f2 = [0 for i in range(n+5)]
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        f2[a[i]] += 1
    for i in range(n):
        f2[a[i]]-=1
        x = f1[a[i]+1]+f1[a[i]+2]
        y = f2[a[i]+1]+f2[a[i]+2]+f2[a[i]]
        ans += x*y
        ans += x*(x-1)//2+y*(y-1)//2
        f1[a[i]]+=1
    print(ans)
