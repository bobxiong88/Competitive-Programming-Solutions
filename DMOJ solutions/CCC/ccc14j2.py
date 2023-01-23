import sys
input = sys.stdin.readline
n = int(input())
v = input()[:n]
a, b = v.count('A'), v.count('B')
if a==b: print('Tie')
elif a>b: print('A')
else: print('B')