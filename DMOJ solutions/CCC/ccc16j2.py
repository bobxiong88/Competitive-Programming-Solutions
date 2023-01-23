g = [list(map(int,input().split())) for i in range(4)]
m = True
for row in g:
    if sum(row)!=sum(g[0]): m = False
for i in range(4):
    s = sum([g[j][i] for j in range(4)])
    if s!=sum(g[0]): m = False
print('magic' if m else 'not magic')