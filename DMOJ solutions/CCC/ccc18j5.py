N = int(input())
graph,visited,long, queue = [list(map(int,input().split()))[1:] for i in range(N)],[True]*2 + [False]*(N-1),float('inf'),[(1,1)]
for node,d in queue:
    if not graph[node-1]: long = min(long,d)
    for n in graph[node-1]:
        if not visited[n]: a,visited[n] = (queue.append((n,d+1))), True
print(str('Y' if all(visited) else 'N')+'\n'+str(long))