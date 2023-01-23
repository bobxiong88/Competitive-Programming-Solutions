import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
s = sum([n*(10**i) for i in range(k+1)])
print(s)