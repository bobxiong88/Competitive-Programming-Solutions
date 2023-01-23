import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a = [abs(i) for i in a]
    for i in range(n):
        if i%2==0:
            a[i] *=-1
    print(" ".join([str(i) for i in a]))
