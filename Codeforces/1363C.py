import sys
input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    n,x = map(int,input().split())
    graph = [[] for i in range(n+1)]
    leaf = []
    for i in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    if len(graph[x])<=1:
        print("Ayush")
        continue
    if n%2:
        print("Ashish")
    else:
        print("Ayush")
