import sys
input = sys.stdin.readline
from math import floor
N, P = map(int,input().split())
gay = []
for i in range(N):
    i, m, cs, e = input().split()
    m = int(m)
    cs = int(cs)
    e = int(e)
    s = floor(4*((m**0.5)-e)+3*(cs**P))
    gay.append((s, i))
print(*reversed(max(gay)))
print(*reversed(min(gay)))