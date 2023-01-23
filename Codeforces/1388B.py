import sys
input = sys.stdin.readline
from math import ceil
for _ in range(int(input())):
    n = int(input())
    gay = ceil(n/4)
    print('9'*(n-gay)+'8'*gay)
