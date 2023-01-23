import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
intervals = [tuple(map(int,input().split())) for i in range(N)]
intervals.sort()
joined = []
L, R = intervals[0]
for l,r in intervals:
    if l <= R+1:
        R = max(R, r)
    else:
        joined.append((L,R))
        L, R = l, r
if (not joined) or (joined and joined[-1] != (L, R)): joined.append((L,R))
queries = [list(map(int,input().split()))+[i] for i in range(Q)]
queries.sort(reverse = True)
joined = joined[::-1]
ans = [0]*Q
while queries and joined:
    L, R, i = queries[-1]
    l, r = joined[-1]
    if r < L:
        ans[i] = 'N'
        joined.pop(-1)
    elif l <= L and R <= r:
        ans[i] = 'Y'
        queries.pop(-1)
    else:
        ans[i] = 'N'
        queries.pop(-1)
    #print(queries, joined)
for L, R, i in queries:
    ans[i] = 'N'
print('\n'.join(ans))