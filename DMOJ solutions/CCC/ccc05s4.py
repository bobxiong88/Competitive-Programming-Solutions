import sys
from collections import deque
input = sys.stdin.readline
L = int(input())
for _ in range(L):
    graph = {}
    n = int(input())
    for i in range(n):
        r = input()
        r = r[:len(r)-1]
        if graph == {}:
            graph.update({r:[]})
            last = r
            continue
        if r not in graph[last]:
            graph[last].append(r)
        try:
            graph[r]
        except:
            graph.update({r:[]})
        if last not in graph[r]:
            graph[r].append(last)
        last = r
    queue = deque([(last, -1, 0)])
    m = -1
    while queue:
        node, last, d = queue.popleft()
        m = max(d, m)
        for i in graph[node]:
            if i!=last:
                queue.append((i, node, d+1))
    print(10*(n-2*m))