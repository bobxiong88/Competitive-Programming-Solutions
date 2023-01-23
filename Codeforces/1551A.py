import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = n//3
    b = n//3
    if n%3 == 1: a += 1
    elif n%3 == 2: b += 1
    print(a,b)
