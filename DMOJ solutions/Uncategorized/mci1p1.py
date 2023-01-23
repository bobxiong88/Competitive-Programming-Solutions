import sys
input = sys.stdin.readline
A, B = map(int,input().split())
for i in range(A+1):
    if i*(A-i) == B:
        print(i, A-i)
        break