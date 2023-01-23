n = int(input())
x, y = 0, 0
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    x+=a[i]
    y+=b[i]
    if x==y: ans = i+1
print(ans)