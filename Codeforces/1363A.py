import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        b.append(a[i]%2)
    b.sort()
    s = sum(b[:x])
    ans = "No"
    if s%2:
        ans = "Yes"
    for i in range(n-x):
        s-=b[i]
        s+=b[i+x]
        if s%2:
            ans = "Yes"
    print(ans)
