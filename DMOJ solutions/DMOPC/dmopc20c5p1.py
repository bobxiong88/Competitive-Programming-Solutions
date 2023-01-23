import sys
input = sys.stdin.readline
S = input().strip('\n')
T = input().strip('\n')
N = len(S)
M = len(T)
cnt = 0
for i in range(min(N,M)):
    if S[i] == T[i]:
        cnt += 1
    else:
        break
print(N+M-2*cnt)