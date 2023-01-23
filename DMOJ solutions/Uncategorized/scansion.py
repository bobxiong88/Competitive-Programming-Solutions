import sys
input = sys.stdin.readline
s = input().strip('\n')
pog ={
"00",
"01",
"10",
"11",
"000",
"001",
"010",
"011",
"100",
"101",
"110",
"111",
"0001",
"0010",
"0011",
"0100",
"0110",
"1000",
"1001"
}
n = len(s)
dp = [0]*(n+1)
dp[0] = 1
s = ' '+s
m=10007
for i in range(2,n+1):
    cnt = 0
    for j in range(max(1, i-3),i):
        c = s[j:i+1]
        if c in pog:
            dp[i] += dp[j-1]
    dp[i]%=m
print(dp[n])