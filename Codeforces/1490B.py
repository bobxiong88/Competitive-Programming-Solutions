import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = [0,0,0]
    for i in a:
        c[i%3] += 1
    ans = 0
    for i in range(6):
        i = i%3
        
        if c[i] < n//3:
            v = n//3-c[i]
            c[i] += v
            c[i-1] -= v
            ans += v
    print(ans)
