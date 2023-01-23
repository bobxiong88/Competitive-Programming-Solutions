import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = a[1:n-1]
    
    if max(b) == 1:
        print(-1)
        continue
    if len(b) == 1 and b[0]%2:
        print(-1)
        continue
    ans = 0
    for i in b:
        ans += (i+1)//2
    print(ans)
