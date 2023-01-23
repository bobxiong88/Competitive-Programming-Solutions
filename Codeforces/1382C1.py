import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in list(input())[:n]]
    b = [int(i) for i in list(input())[:n]]
    ans = []
    for i in range(-1,-n-1,-1):
        if a[i]!=b[i]:
            if a[0]!=a[i]:
                ans.append(1)
                a[0] = abs(a[0]-1)
            ans.append(n+i+1)
            sub = list(reversed(a[:n+i+1]))
            for j in range(n+i+1):
                a[j] = abs(sub[j]-1)
    print(len(ans)," ".join([str(i) for i in ans]))
