import sys
input = sys.stdin.readline
def top(node, visited, order):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            top(n, visited, order)
    order.append(node)
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
graph = [[],[7,4],[1],[4,5],[],[],[],[]]
i = 0
while True:
    n = int(input())
    if i%2==0:
        last = n
    else:
        if not n: break
        graph[last].append(n)
    i+=1
visited = [False]*8
stack = [False]*8
for node in range(1,8):
    if not visited[node]:
        if cycle(node, visited, stack):
            print("Cannot complete these tasks. Going to bed.")
            sys.exit(0)
order = []
visited = [False]*8
for node in range(7,0,-1):
    if not visited[node]:
        top(node, visited, order)
print(" ".join([str(i) for i in order[::-1] ]))