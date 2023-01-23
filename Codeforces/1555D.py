import sys
input = sys.stdin.readline
n, m = map(int,input().split())
s = input().strip('\n')
k = n//3+n%3
ligma = ['abc'*k, 'acb'*k, 'bac'*k, 'bca'*k, 'cba'*k, 'cab'*k]
psa = [[0 for i in range(n+1)] for j in range(6)]
for i in range(6):
    for j in range(1,n+1):
        psa[i][j] = psa[i][j-1]+(ligma[i][j-1]!=s[j-1])
for i in range(m):
    l, r = map(int,input().split())
    ans = float('inf')
    for x in range(6):
        ans = min(ans, psa[x][r]-psa[x][l-1])
    print(ans)
    
