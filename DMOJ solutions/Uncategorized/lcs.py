m,n = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
C = [[0]*(m+1) for i in range(n+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if X[i-1]==Y[j-1]:
            C[j][i] = C[j-1][i-1]+1
        else:
            C[j][i] = max(C[j][i-1],C[j-1][i])
print(C[n][m])