import sys
input = sys.stdin.readline
S = input().strip('\n')
cnt = [0]*26
for i in S: cnt[ord(i)-ord('a')] += 1
ans = 1
for i in cnt:
    ans *= i+1
    ans %= int(1e9)+7
print(ans)