import sys
input = sys.stdin.readline
from collections import deque
import random
start = [input().split() for i in range(3)]
for i in range(3):
    for j in range(3):
        if start[i][j] != 'X': start[i][j] = int(start[i][j])
def row(grid):
    for i in range(3):
        if grid[i][0] != 'X' and grid[i][1] != 'X' and grid[i][2] == 'X':
            grid[i][2] = 2*grid[i][1]-grid[i][0]
            return True
        if grid[i][1] != 'X' and grid[i][2] != 'X' and grid[i][0] == 'X':
            grid[i][0] = 2*grid[i][1]-grid[i][2]
            return True
    return False
def col(grid):
    for j in range(3):
        if grid[0][j] != 'X' and grid[1][j] != 'X' and grid[2][j] == 'X':
            grid[2][j] = 2*grid[1][j]-grid[0][j]
            return True
        if grid[1][j] != 'X' and grid[2][j] != 'X' and grid[0][j] == 'X':
            grid[0][j] = 2*grid[1][j]-grid[2][j]
            return True
    return False
def mrow(grid):
    for i in range(3):
        if grid[i][0] != 'X' and grid[i][2] != 'X' and grid[i][1] == 'X':
            grid[i][1] = (grid[i][0]+grid[i][2])//2
            return True
    return False
def mcol(grid):
    for j in range(3):
        if grid[0][j] != 'X' and grid[2][j] != 'X' and grid[1][j] == 'X':
            grid[1][j] = (grid[0][j]+grid[2][j])//2
            return True
    return False
def check(grid):
    for i in range(3):
        if grid[i][0]+grid[i][2] != 2*grid[i][1]: return False
        if grid[0][i]+grid[2][i] != 2*grid[1][i]: return False
    return True
queue = deque([start])
while queue:
    # two in a row
    grid = queue.popleft()
    #print(queue)
    if row(grid) or col(grid) or mrow(grid) or mcol(grid):
        queue.appendleft(grid)
    else:
        found = False
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 'X':
                    a = [i[:] for i in grid]
                    b = [i[:] for i in grid]
                    a[i][j] = random.randint(-3000000,3000000)
                    b[i][j] = a[i][j]-1
                    queue.appendleft(a)
                    queue.appendleft(b)
                    found = True
        if not found:
            if check(grid):
                for i in grid:
                    print(*i)
                break