import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in list(input())[:n]]
    b = [int(i) for i in list(input())[:n]]
    ans = []
    c = []
    for i in range(1,n):
        if a[i]!=a[i-1]:
            ans.append(i)
    if a[-1]!=b[-1]:
        ans.append(n)
    for i in range(1,n):
        if b[i]!=b[i-1]:
            c.append(i)
    ans = ans + c[::-1]
    print(len(ans)," ".join([str(i) for i in ans]))
