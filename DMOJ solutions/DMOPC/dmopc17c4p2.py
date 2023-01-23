import sys
input = sys.stdin.readline
from collections import deque
def bfs(x,y):
    queue = deque([(x, x, [])])
    while queue:
        node, p, arr = queue.popleft()
        arr.append(a[node])
        if node == y:
            return arr
        for n in graph[node]:
            if n == p: continue
            queue.append((n, node, arr[:]))
N, Q = map(int,input().split())
graph = [[] for i in range(N+1)]
a = [0]+list(map(int,input().split()))
for i in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(Q):
    q,x,y = map(int,input().split())
    arr = sorted(bfs(x,y))
    #print(arr)
    if q == 1:
        ans = sum(arr)/len(arr)
    elif q == 2:
        if len(arr)%2:
            ans = arr[len(arr)//2]
        else:
            ans = arr[len(arr)//2]+arr[len(arr)//2-1]
            ans /= 2
    else:
        mx = 0
        ans = 0
        curr = 0
        cnt = 0
        for i in arr:
            cnt += 1
            if i != curr: cnt = 1
            if cnt > mx:
                mx = cnt
                ans = i
            curr = i
    print(int(ans+0.5))