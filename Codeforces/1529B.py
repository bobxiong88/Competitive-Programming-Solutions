import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    neg = []
    pos = []
    for i in a:
        if i<=0:
            neg.append(i)
        else:
            pos.append(i)
    neg.sort()
    m = float('inf')
    ans = len(neg)
    for i in range(len(neg)-1):
        m = min(m, abs(neg[i]-neg[i+1]))
    for i in pos:
        if i <= m:
            ans += 1
            break
    print(ans)
