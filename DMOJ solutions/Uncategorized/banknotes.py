import sys
input = sys.stdin.readline
n = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
obj = [(b[i], c[i]) for i in range(n)]
obj.sort(reverse = True)
k = int(input())
dp = [[float('inf'), 0] for i in range(k+1)]
dp[0][0] = 0
for i in range(n):
    for x in range(obj[i][0], k+1):
        if dp[x-obj[i][0]][0] != float('inf'):
            if dp[x-obj[i][0]][1] < obj[i][1]:
                if dp[x-obj[i][0]][0]+1 < dp[x][0]:
                    dp[x][0] = dp[x-obj[i][0]][0]+1
                    dp[x][1] = dp[x-obj[i][0]][1]+1
    for i in range(obj[i][0],k+1):
        dp[i][1] = 0
print(dp[k][0])