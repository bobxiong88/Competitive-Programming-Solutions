import sys
input = sys.stdin.readline
from math import log
n = int(input())
n = bin(n)[2:]
c = 0
for i in n:
    if i == '1':
        c+=1
print(c)
