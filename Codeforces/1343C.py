import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    subs = []
    sub = []
    for i in a:
        if sub and i//abs(i)!=sub[-1]//abs(sub[-1]):
            subs.append(sub)
            sub = []
        sub.append(i)
    if sub: subs.append(sub)
    ans = 0
    for sub in subs: ans += max(sub)
    print(ans)
