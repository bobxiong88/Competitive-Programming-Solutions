import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = "YES"
    for i in range(n-1):
        if a[i+1]-a[i]>1:
            ans = "NO"
    print(ans)
