import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
a.sort()
x=sum(a[:N])
y=sum(a)-x
print(abs(x-y))