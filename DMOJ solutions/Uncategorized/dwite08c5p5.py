import sys
from collections import deque
input = sys.stdin.readline
for _ in range(5):
    p = int(input())
    n = int(input())
    letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
    dist = {}
    graph = {}
    for letter in letters:
        graph.update({letter:[]})
        dist.update({letter:float('inf')})
    poo = 0
    for i in range(n):
        q, d = input().split()
        a,b = tuple(q)
        d = list(d)
        for c, x in enumerate(d):
            if x=="x":
                d[c] = str(p)
                poo +=1
        w = eval("".join(d))
        graph[a].append((b,w))
    queue = deque([("A",0)])
    dist['A'] = 0
    while queue:
        node, d = queue.popleft()
        #print(node, d, queue)
        if d>dist[node]:
            continue
        for n,w in graph[node]:
            if dist[n] > d + w:
                dist[n] = d+w
                queue.append((n, d+w))
    # what the fuck am i doing
    print(int(dist['Z'])- (1 if poo>1 else 0))
