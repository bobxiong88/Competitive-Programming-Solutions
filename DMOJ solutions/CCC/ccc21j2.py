import sys
input = sys.stdin.readline
m = 0
for i in range(int(input())):
    a = input()
    b = int(input())
    if b > m: n, m = a, b
print(n)