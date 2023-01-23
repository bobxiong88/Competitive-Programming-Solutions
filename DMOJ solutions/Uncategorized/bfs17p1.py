ans = 0
N = int(input())
for i in input().split():
    if len(i)>10:
        ans += 1
print(N-ans)