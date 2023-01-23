import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    p,q = 0,0
    A = [[0]*n for i in range(n)]
    for i in range(1,k+1):
        A[p][q] = 1
        p+=1
        q=(q+1)%n
        if p==n:
            p = 0
            q = (q+1)%n
    maxC = -1
    minC = float("inf")
    for i in range(n):
        c = 0
        for j in range(n):
            c+=A[j][i]
        maxC = max(maxC,c)
        minC = min(minC,c)
    maxR = -1
    minR = float("inf")
    for i in range(n):
        r = sum(A[i])
        maxR = max(maxR, r)
        minR = min(minR, r)
    print((maxR-minR)**2+(maxC-minC)**2)
    for row in A:
        print("".join([str(i) for i in row]))
