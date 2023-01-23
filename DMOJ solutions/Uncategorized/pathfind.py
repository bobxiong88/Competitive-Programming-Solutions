import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int,input().split())
walls = dict()
for i in range(K):
    walls.update({tuple(map(int,input().split())):False})
for w in walls:
    if not walls[w]:
        walls[w] = True
        queue = deque([w])
        left, up, right, down = [False]*4
        while queue:
            x,y = queue.popleft()
            if y==1: left = True
            elif y==M: right = True
            if x==1: up = True
            elif x==N: down = True
            for a,b in (1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1):
                i,j = x+a,y+b
                if (i,j) in walls:
                    if not walls[(i,j)]:
                        queue.append((i,j))
                        walls[(i,j)] = True
        if (up and down) or (left and right) or (left and up) or (right and down):
            print("NO")
            sys.exit(0)
print("YES")