import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    ans = 1
    f = []
    if k<n:
        for i in range(1, int(n**0.5)+1):
            if n%i==0 and i<=k:
                f.append(i)
                if n//i<=k:
                    f.append(n//i)
        m = max(f)
        ans = n//m
    print(ans)
        
