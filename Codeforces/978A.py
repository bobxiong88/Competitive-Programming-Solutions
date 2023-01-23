import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(-1,-n-1,-1):
    if a[i] not in b: b.append(a[i])
b = b[::-1]
print(len(b))
print(*b)
