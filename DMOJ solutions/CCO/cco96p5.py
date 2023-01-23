def bfs(graph,A,B):
    visited = [A]
    queue = [(A,[A])]
    while queue:
        node, path = queue.pop()
        if node==B:
            return "".join(path)
        for n in graph[node]:
            if n not in visited:
                queue.append((n,path+[n]))
                visited.append(n)
    
N,Q = [int(i) for i in input().split()]
graph = {}
for i in range(N):
    A,B = input().split()
    A = A[:1]
    B = B[:1]
    try:
        graph[A].append(B)
    except:
        graph.update({A:[B]})
    try:
        graph[B].append(A)
    except:
        graph.update({B:[A]})
for i in range(Q):
    A,B = input().split()
    A = A[:1]
    B = B[:1]
    print(bfs(graph,A,B))