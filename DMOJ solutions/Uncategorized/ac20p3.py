import sys
input = sys.stdin.readline
def get(c):
    return ord(c)-ord('a')
N, M = map(int,input().split())
S = input().strip('\n')
T = input().strip('\n')
first = [[-1]*26 for i in range(N+1)]
for i in range(N,-1,-1):
    if i != N:
        first[i] = first[i+1][:]
        first[i][get(S[i])] = i+1
for i in T:
    if first[0][get(i)] == -1:
        print(-1)
        sys.exit(0)
x = 0
ans = 0
cnt = 0
for i in T:
    if first[x][get(i)] == -1:
        cnt += 1
        ans = cnt*N
        x = 0
    ans += first[x][get(i)]-x
    x = first[x][get(i)]
print(ans)