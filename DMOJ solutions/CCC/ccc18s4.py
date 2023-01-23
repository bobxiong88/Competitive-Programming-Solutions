import sys
input = sys.stdin.readline
def solve(x):
    if x in dp: return dp[x]
    dp[x] = 0
    for i in range(1,int(x**0.5)+1):
        dp[x] += solve(i)*((x//i)-(x//(i+1)))
        if i >= 2 and i!=x//i: dp[x] += solve(x//i)
    return dp[x]
N = int(input())
dp = {}
dp[1] = 1
print(solve(N))