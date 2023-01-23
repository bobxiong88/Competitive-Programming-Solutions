N = int(input())


weight = [0]*(N+1)
value = [0]*(N+1)

for i in range(1,N+1):
    w,v = map(int,input().split())
    weight[i],value[i] = int(w/2)+1,v
    
sumValue = sum(value)
dp = [float('inf')]*(sumValue+1)
dp[0]=0

for item in range(1,N+1):
    for x in range(sumValue-value[item],-1,-1):
        dp[x+value[item]] = min(dp[x+value[item]],dp[x]+weight[item])


print(min(dp[int(sumValue/2)+1:sumValue+1]))