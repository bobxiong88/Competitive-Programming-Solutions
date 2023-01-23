ans = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    ans = max(ans, b-a)
print(ans)