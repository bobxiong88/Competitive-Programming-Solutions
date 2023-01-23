import sys
input = sys.stdin.readline
N = int(input())
chore = []
for i in range(N):
    a,b = map(int,input().split())
    chore.append((a,b))
chore.sort()
ans = 0
curr = 0
m = int(1e9)+7
for a,b in chore:
    ans += curr*b+a*b*(b+1)//2
    ans %= m
    curr += a*b
    curr %= m
    #print(curr)
print(ans)