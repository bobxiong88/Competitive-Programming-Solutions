import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, x, y = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a)
    if (x+s)%2 == y%2: print("Alice")
    else: print("Bob")
