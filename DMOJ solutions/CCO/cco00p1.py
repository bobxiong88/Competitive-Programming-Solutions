def dfs(graph,letter,elements,visited):
    if visited[letter]==False:
        visited[letter]=True
        for n in graph[letter]:
            if n.lower()!=n:
                dfs(graph,n,elements,visited)
            else:
                elements.append(n)
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercases  = list(capitals.lower())
capitals = list(capitals)
N = int(input())
graph = {}
lettersUsed = []
for i in capitals:
    graph.update({i:set()})
for i in range(N):
    A, _, B = input().split()
    graph[A].update(B)
    
    lettersUsed.append(A)
    if B.lower()!=B:
        lettersUsed.append(B)
alphaOrder = sorted(list(graph.keys()))
lettersUsed = set(lettersUsed)
lettersUsed = sorted(lettersUsed)
for letter in lettersUsed:
    visited = {}
    for l in alphaOrder:
        visited.update({l:False})
    elements = []
    dfs(graph,letter,elements,visited)
    elements = set(elements)
    elements = sorted(elements)
    print(letter,"=","{"+",".join(elements)+"}")