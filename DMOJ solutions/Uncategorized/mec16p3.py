import sys
input = sys.stdin.readline
N, T = map(int,input().split())
dp = [0]*(T+1)
for i in range(N):
    a = []
    skill = list(map(int,input().split()))
    L = skill[0]
    tw = 0
    tv = 0
    for x in range(1,L+1):
        tw += skill[x*2-1]
        tv += skill[x*2]
        a.append((tw, tv))
    for j in range(T, -1, -1):
        for w,v in a:
            if j+w <= T:
                dp[j+w] = max(v+dp[j], dp[j+w])
print(dp[-1])