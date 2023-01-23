import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = []
    s = 0
    for i in range(1,n+1):
        a.append(2**i)
    s+=a.pop()
    for i in range(n//2-1):
        s+=a.pop(0)
    print(abs(sum(a)-s))
