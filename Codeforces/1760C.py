import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    s = list(map(int,input().split()))
    a = sorted(s)
    ans = []
    for i in range(n):
        if s[i] == a[-1]:
            ans.append(s[i]-a[-2])
        else:
            ans.append(s[i]-a[-1])
    print(*ans)
