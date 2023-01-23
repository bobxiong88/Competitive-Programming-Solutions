import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    bks = [-1]
    for i in range(n-1):
        if a[i] >= 2*a[i+1]:
            bks.append(i)
    bks.append(n-1)
    ans = 0
    for i in range(len(bks)-1):
        diff = bks[i+1]-bks[i]
        if diff >= k+1:
            ans += diff-(k+1)+1
    print(ans)
