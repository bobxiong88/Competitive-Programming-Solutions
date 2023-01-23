import sys
from collections import deque
input = sys.stdin.readline
def cycle(node, visited, stack):
    visited[node] = True
    stack[node] = True
    for n in graph[node]:
        if not visited[n]:
            if cycle(n,visited,stack):
                return True
        elif stack[n]:
            return True
    stack[node] = False
    return False
N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
visited= [False]*(N+1)
stack = [False]*(N+1)
for n in range(1,N+1):
    if not visited[n]:
        if cycle(n, visited, stack):
            print("N")
            sys.exit(0)
print("Y")