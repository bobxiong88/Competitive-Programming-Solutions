import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        print(n//2, n//2)
        continue
    found = False
    for i in range(2, int(n**0.5+1)):
        if n%i==0:
            print(n//i, n-n//i)
            found = True
            break
    if not found:
        print(1, n-1)
