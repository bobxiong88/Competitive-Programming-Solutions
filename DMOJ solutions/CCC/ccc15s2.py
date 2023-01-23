import sys
input = sys.stdin.readline
J = int(input())
A = int(input())
a = []
for i in range(J):
    s = input().strip('\n')
    a.append('SML'.index(s))
ans = 0
for i in range(A):
    x,y = input().split()
    y = int(y)
    x = 'SML'.index(x)
    if a[y-1] >= x:
        ans += 1
        a[y-1] = -1
print(ans)