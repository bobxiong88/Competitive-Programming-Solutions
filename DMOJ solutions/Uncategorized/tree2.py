import sys
def d(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
from collections import deque
input = sys.stdin.readline
R, C = map(int,input().split())
graph = []
for i in range(R):
    graph.append(input().split())
heights = [[] for i in range(10)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == "X":
            start = (i,j)
        if graph[i][j] == "." or graph[i][j] == "X":
            graph[i][j] = 0
        else:
            graph[i][j] = int(graph[i][j])
            heights[graph[i][j]].append((i,j))
for c, height in enumerate(list(reversed(heights))):
    if height!=[]:
        trees = height
        height = 9-c
        break
m, close = float('inf'), 0
for tree in trees:
    if m>d(tree, start):
        m = d(tree, start)
        close = tree
dist = [[[float('inf'), float('inf')] for i in range(C)] for i in range(R)]
queue = deque([(start,0,0)])
dist[start[0]][start[1]][0] = 0
dist[start[0]][start[1]][1] = 0
while queue:
    node, d, num = queue.popleft()
    y, x = node
    if d>dist[y][x][0] or num>dist[y][x][1]:
        continue
    pos = []
    pos.append((y+1,x))
    pos.append((y,x+1))
    pos.append((y-1,x))
    pos.append((y,x-1))
    for p in pos:
        i, j = p
        if 0<=i<R and 0<=j<C:
            curr = d + graph[i][j]
            n = int(str(num))
            if graph[i][j]!=0:
                n+=1
            if curr < dist[i][j][0] or (curr==dist[i][j][0] and n<dist[i][j][1]):
                dist[i][j][0] = curr
                dist[i][j][1] = n
                queue.append((p, curr, n))
ans = dist[close[0]][close[1]][1]-1
print(ans)