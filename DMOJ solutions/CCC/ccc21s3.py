import sys
input = sys.stdin.readline
N = int(input())
cum = 0
de = {}
for i in range(N):
    P, W, D = map(int,input().split())
    s = max(P-D, 0)
    cum += W*s
    if 1 in de: de[1] -= W
    else: de[1] = -W
    if s+1 in de: de[s+1] += W
    else: de[s+1] = W
    k = P+D+1
    if k in de: de[k] += W
    else: de[k] = W
last = 0
gamer = 0
ans = cum
for i in sorted(de):
    cum += gamer*(i-last)
    ans = min(ans,cum)
    gamer += de[i]
    last = i
print(ans)