import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
if n==1:
    print(1,1)
    print(0)
    print(1,1)
    print(0)
    print(1,1)
    print(-a[0])
    sys.exit(0)
m = n-1
o1 = []
for i in range(m):
    o1.append(a[i]*m)
    a[i] = a[i]*m+a[i]
print(1,m)
print(*o1)
print(n,n)
print(n-a[-1])
a[-1] = n
print(1,n)
a = [-i for i in a]
print(*a)
