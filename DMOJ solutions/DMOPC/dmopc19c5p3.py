import sys
input = sys.stdin.readline
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
N, M = map(int,input().split())
count = 0
for x in range(1,N):
    for y in range(M):
        dx = y/gcd(x,y)
        dy = x/gcd(x,y)
        xi = x+dx
        yi = y+dy
        while 1<=xi<=N and 1<=yi<=M:
            count+=(M-yi)*(N-xi)
            xi+=dx
            yi+=dy
print(int(count))