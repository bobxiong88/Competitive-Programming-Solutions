import sys
input = sys.stdin.readline
a = [tuple(map(int,input().split())) for i in range(int(input()))]
s = int(input())
dp = [[0,0] for i in range(s+1)]
for H, E, P in a:
    items = []
    i = 1
    T = H
    while P*i <= s:
        items.append((T, P*i, i))
        T += H-E*i
        i += 1
    for i in range(s, -1, -1):
        for v, w, t in items:
            if i+w <= s:
                if v+dp[i][0] > dp[i+w][0]:
                    dp[i+w][0] = v+dp[i][0]
                    dp[i+w][1] = t+dp[i][1]
                elif v+dp[i][0] < dp[i+w][0]:
                    pass
                else:
                    dp[i+w][1] = min(dp[i+w][1], dp[i][1]+t)
    #print(dp)
    #print(items)
print(dp[s][0])
print(dp[s][1])