N = int(input())
M = int(input())
ans = 0
for i in range(M):
    if int(input()) >= N:
        ans += 1
print(ans)