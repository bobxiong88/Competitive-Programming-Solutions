import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = [0,0,0]
ans = [0,0,0]
for i in range(n): s[i%3] += a[i]
for i in range(n):
    for j in range(3):
        ans[(i+j)%3] += s[(i-j)%3]*b[i]
print(*ans[::-1])