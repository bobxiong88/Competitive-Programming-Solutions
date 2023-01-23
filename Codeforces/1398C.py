import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,list(input()[:n])))
    ans = 0
    d = [0]*(n*10)
    x = 0
    for i in range(n):
        d[x] += 1
        x += a[i]-1
        ans += d[x]
    print(ans)
        
            
