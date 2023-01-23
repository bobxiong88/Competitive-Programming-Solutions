import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 0
    sa = min(a)
    sb = min(b)
    for i in range(n):
        ans += max(a[i]-sa, b[i]-sb)
    print(ans)
    
