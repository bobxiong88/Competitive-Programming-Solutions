import sys
input = sys.stdin.readline
n1, n2, n3 = map(int,input().split())
a = []
for i in range(3):
    a.append(list(map(int,input().split())))
for i in range(3):
    a[i].sort()
    #print(a[i], sum(a[i]))
ans = -float('inf')
for i in range(3):
    x = i
    y = (i+1)%3
    z = (i-1)%3
    curr = sum(a[x])
    ys = sum(a[y])
    zs = sum(a[z])
    k = ys+zs
    curr += k
    curr -= min(2*ys,2*zs,2*(a[y][0]+a[z][0]))
    ans = max(ans, curr)
    #print(curr)
print(ans)
