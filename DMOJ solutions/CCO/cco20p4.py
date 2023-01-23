import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
g = [[0]*(N) for i in range(N)]
for i in range(1,N):
    c = input().strip('\n')
    for j in range(i):
        if c[j] == 'B':
            g[i][j] = 1
            g[j][i] = 1
# [b, b, b, b, b]--------[r, r, r, r, r]
#           FREE SEX JUNCTION
for i in range(N):
    bbc = []
    for j in range(N):
        if j != i: bbc.append(j)
    bbc.append(i)
    cock = deque([])
    for v in bbc:
        if len(cock)<2: cock.append(v)
        elif g[cock[0]][v] == 0: cock.appendleft(v)
        elif g[cock[-1]][v] == 1: cock.append(v)
        # racism case
        else:
            if g[cock[0]][cock[-1]] == 0:
                cock.appendleft(cock.pop())
                cock.appendleft(v)
            else:
                cock.append(cock.popleft())
                cock.append(v)
    print(N)
    cock = list(cock)
    for k in range(N):
        cock[k]+=1
    if cock[-1] == i+1: cock = cock[::-1]
    print(*cock)
#print(g)