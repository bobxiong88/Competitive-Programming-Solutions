import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
s1 = 0
s2 = 0
for i in range(n):
    nxt = max(s1,s2)
    s1 = s2+a[i]
    s2 = nxt
print(max(s1,s2))