import sys
sys.setrecursionlimit(15000)

def findFriend(graph,ox, x, y, visited):
    nodeVal = graph[x]
    visited.append(nodeVal)

    if nodeVal==-1:
        pass
    elif ox == nodeVal:
        pass
    else:
        findFriend(graph,ox,nodeVal,y,visited)
    return visited

graph = {}

for i in range(1,1000):
    graph.update({i:-1})
graph.update({-1:-1})
graph.update({0:-1})
n = int(input())
for i in range(n):
    x, y = [int(i) for i in input().split()]
    graph[x] = y
while True:
    x, y = [int(i) for i in input().split()]
    if (x,y) == (0,0):
        break
    
    circle = findFriend(graph,x, x, y, [])
    if x not in circle or y not in circle:
        print("No")
    else:
        print("Yes",circle.index(y))