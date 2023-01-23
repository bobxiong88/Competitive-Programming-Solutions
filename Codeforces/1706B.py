import sys
input = sys.stdin.readline
from math import ceil
for _ in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    freq = [[] for i in range(n+1)]
    for i in range(n):
        freq[c[i]].append(i)
    res = []
    for x in range(1,n+1):
        if not freq[x]:
            res.append(0)
            continue
        '''

        new = [freq[x][0]]
        for i in range(len(freq[x])):
            if freq[x][i]%2 != new[-1]:
                new.append(freq[x][i])
        res.append(ceil(len(new)/2))
        '''
        dp = [[0,0] for i in range(len(freq[x]))]
        dp[0] = [1,0]
        for i in range(1,len(freq[x])):
            
            p = freq[x][i]-freq[x][i-1]
            p = p%2
            if p == 1:
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        res.append(max(dp[-1]))
    print(*res)
