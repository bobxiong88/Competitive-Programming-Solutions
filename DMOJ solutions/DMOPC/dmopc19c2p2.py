N, M  = map(int,input().split())
dp = [[float('inf')]*M for i in range(N)]
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

dp[0][0] = graph[0][0]
queue = [(0,0)]
while queue:
    y,x = queue.pop(0)
    distance = dp[y][x]
    ps = []
    ps.append((y+1,x))
    ps.append((y,x+1))
    for p in ps:
        if 0<=p[0]<N and 0<=p[1]<M:
            if distance+graph[p[0]][p[1]]<dp[p[0]][p[1]]:
                queue.append(p)
                dp[p[0]][p[1]] = distance+graph[p[0]][p[1]]
print(dp[N-1][M-1])