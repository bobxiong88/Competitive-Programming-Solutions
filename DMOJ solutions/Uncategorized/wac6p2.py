import sys
input = sys.stdin.readline
N, M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b = [i-1 for i in b]
on = a.count(1)
if not on:
    print(0)
    sys.exit(0)
i = 0
while True:
    if i<M:
        if a[b[i]]:
            on -= 1
        else:
            on += 1
        a[b[i]] ^= 1
    if on <= i+1:
        print(i+1)
        break
    i += 1