import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a = a[::-1]
    ans = 0
    c = 0
    for i in range(n):
        c += 1
        if c*a[i] >= x:
            ans += 1
            c = 0
    print(ans)
    #print(a)
