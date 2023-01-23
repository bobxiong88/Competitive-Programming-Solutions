import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x,y,n = map(int,input().split())
    a = int((n-y)/x)
    print(a*x+y)
