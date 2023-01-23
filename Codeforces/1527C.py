import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    mp = dict()
    ans = 0
    for i in range(n):
        if a[i] not in mp:
            mp[a[i]] = 0
        ans += mp[a[i]]*(n-i)
        mp[a[i]]+=i+1
    print(ans)
