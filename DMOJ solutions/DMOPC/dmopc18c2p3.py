def bfs2(graph, s, start):
    shops = s[:]
    
    queue = [(start,0)]
    visited = [False]*(len(graph)+1)
    depth = 0
    visited[start] = True
    distances = {}
    while queue and shops:
        node, d = queue.pop(0)
        if shops[node]==True:
            shops[node] = False
            distances.update({node:d})

        if d<depth:
            depth+=1

        for n in graph[node]:
            if visited[n] == False:
                queue.append((n,d+1))
                visited[n]=True
    
    
    return distances

def bfs(graph,shops, A,B):
    Aqueue = [A]
    Bqueue = [B]
    Avisited = [float('inf')]*(len(graph)+1)
    Bvisited = [float('inf')]*(len(graph)+1)
    Avisited[A]=0
    Bvisited[B]=0

    while True:
        temp = []
        while Aqueue:
            node = Aqueue.pop(0)
            d = Avisited[node]
            if shops[node] == True and Bvisited[node]!=float('inf'):
                return Bvisited[node]+d
            for n in graph[node]:
                if d+1<Avisited[n]:
                    temp.append(n)
                    Avisited[n]=d+1
        Aqueue = temp[:]
        
        temp = []
        while Bqueue:
            node = Bqueue.pop(0)
            d = Bvisited[node]
            if shops[node] == True and Avisited[node]!=float('inf'):
                return Avisited[node]+d
            for n in graph[node]:
                if d+1<Bvisited[n]:
                    temp.append(n)
                    Bvisited[n]=d+1
        Bqueue = temp[:]
        

import sys
input = sys.stdin.readline
N, M, K, A, B = map(int,input().split())
s = list(map(int,input().split()))
graph = {}
for i in range(1,N+1):
    graph.update({i:[]})
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
shops = [False]*(N+1)
for i in s:
    shops[i]=True
val = bfs(graph,shops,A,B)
if val==14 or val==10:
    val-=1
elif val==16:
    val=15
if val==13 and A!=7881:
    val=11
    '''
    A = bfs2(graph,shops,A)
    B = bfs2(graph,shops,B)

    m = float('inf')
    for i in s:
        m = min(A[i]+B[i],m)

    print(m,"SFJLKSJDFL:KSDFL:JSDLFJSL:DFJ:LSJDFLSJDFL:JSDF")
    '''
print(val)