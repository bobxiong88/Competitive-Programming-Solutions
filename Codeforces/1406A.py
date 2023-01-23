import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    flag = False
    for i in range(n):
        if i in a:
            a.remove(i)
        else:
            ans+=i
            flag = True
            break
    if not flag: ans+=n
    flag = False
    for i in range(n):
        if i in a:
            a.remove(i)
        else:
            ans+=i
            flag = True
            break
    if not flag: ans += n
    print(ans)
