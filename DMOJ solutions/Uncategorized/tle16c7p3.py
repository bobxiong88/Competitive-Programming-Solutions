import sys
input = sys.stdin.readline
N = int(input())
A = [0]+list(map(int,input().split()))
k = 0
K = [0]
for i in range(1, N+1):
    if A[i] == 1:
        k = i
    K.append(k)
Q = int(input())
for i in range(Q):
    x, y = map(int,input().split())
    k = K[y]
    if k<x:
        if (y-x)%2==0:
            print(0)
        else:
            print(1)
    if k == x:
        if (y-x)%2==0:
            print(1)
        else:
            print(0)
    if k>x:
        if (y-k)%2:
            print(1)
        else:
            print(0)