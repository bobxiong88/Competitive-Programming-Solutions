import sys
input = sys.stdin.readline
test = int(input())
for t in range(test):
    pins, balls, width = map(int,input().split())
    pin  =[]
    for i in range(pins):
        pin.append(int(input()))

    s = 0
    sums = [0]*pins
    for i in range(width):
        s+=pin[i]
    sums[0] = s
    for i in range(1,pins-width+1):
        s = s - pin[i-1] + pin[i+width-1]
        sums[i] = s
    dp = [[0]*(pins) for i in range(balls+1)]

    for i in range(1,balls):
        for j in range(pins):
            dp[i][j] = -1
            
    for b in range(1, balls+1):
        for i in range(pins-1,-1,-1):
            if i>=pins-width:
                dp[b][i] = sums[i]
            else:
                dp[b][i] = max(dp[b-1][i+width]+sums[i],dp[b][i+1])
    print(dp[balls][0])