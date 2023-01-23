import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    ans, s = 0,0
    for i in range(n):
        s+=a[i]
        if s/(i+1)>=x: ans = i+1
    print(ans)
