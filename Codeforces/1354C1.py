import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    n*=2
    a = (n-2)*180/n
    print(math.tan(math.radians(a/2)))
