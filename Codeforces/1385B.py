import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    p = []
    for i in range(n*2):
        if a[i] not in p:
            p.append(a[i])
    print(" ".join([str(i) for i in p]))
