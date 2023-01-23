import sys
input = sys.stdin.readline
def heron(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
def radius(a,b,c):
    return a*b*c/(4*heron(a,b,c))
def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
n = int(input())
p = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a,b,c = sorted([dist(p[i],p[j]), dist(p[i],p[k]), dist(p[j],p[k])])
            if a**2+b**2<c**2:
                ans = max(ans, c)
            else:
                ans = max(ans, radius(a,b,c)*2)
print("{:0.2f}".format(ans))