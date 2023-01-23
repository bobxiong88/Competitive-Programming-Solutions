import sys
input = sys.stdin.readline
mx = int(1e5)+5
N = int(input())
val = [[] for i in range(mx)]
for i in range(N):
    a,b = map(int,input().split())
    val[a+b].append((a,b))
ans = 0
for x in range(mx):
    val[x].sort()
    pk = sum([a for a, b in val[x]])
    pm = 0
    for i in range(len(val[x])):
        a,b = val[x][i]
        pm += b
        pk -= a
        ans = max(ans, min(pm, pk))
print(ans)