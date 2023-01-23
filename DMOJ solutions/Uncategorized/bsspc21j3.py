import sys
input = sys.stdin.readline
ans = [0,0,0]
M, N = map(int,input().split())
for i in range(N):
    a = input().strip('\n')
    g = [[0]*M for t in range(3)]
    for j in range(M):
        if a[j] == 'R':
            g[0][j] = 1
        elif a[j] == 'U':
            g[2][j] += 1
        elif a[j] == 'Y':
            g[1][j] +=1
        elif a[j] == 'O':
            g[0][j] += 1
            g[1][j] += 1
        elif a[j] == 'G':
            g[2][j] += 1
            g[1][j] += 1
        elif a[j] == 'P':
            g[0][j] += 1
            g[2][j]+=1
        elif a[j] == 'B':
            g[0][j]+=1
            g[2][j] +=1
            g[1][j] +=1
    for k in range(3):
        for j in range(M):
            if j:
                if g[k][j] == 1 and g[k][j-1] != 1:
                    ans[k] += 1
            else:
                if g[k][j] == 1:
                    ans[k]+=1
print(*ans)