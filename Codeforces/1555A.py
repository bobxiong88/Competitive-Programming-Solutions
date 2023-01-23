import sys
from math import ceil
input = sys.stdin.readline
from itertools import permutations
s = [6,8,10]
t = [15,20,25]
for _ in range(int(input())):
    n = int(input())
    ans = float('inf')
    if n<=6:
        print(15)
    else:
        print((n//2+n%2)*5)
