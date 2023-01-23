import sys
from math import *
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    n*=2
    print(cos(pi/(2*n))/sin(pi/n))
