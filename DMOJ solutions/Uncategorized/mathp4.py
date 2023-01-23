import sys
import math
input = sys.stdin.readline
def area(a, b):
    return math.asin(b)+b*math.sqrt(1-b**2)-math.asin(a)-a*math.sqrt(1-a**2)
N = int(input())
s = math.pi/N
prev = -1
res = []
for i in range(N-1):
    l = prev
    r = 1
    while abs(l-r) >= pow(10, -12):
        m = (l+r)/2
        if area(-1, m) > s*(i+1):
            r = m
        else:
            l = m
    prev = r
    print('{0:.9f}'.format(r))