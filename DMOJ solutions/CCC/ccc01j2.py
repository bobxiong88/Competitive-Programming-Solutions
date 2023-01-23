x = int(input())
m = int(input())
ans = 0
for i in range(1,m):
    if i*x%m==1:
        ans = i
        break
if not ans: ans = 'No such integer exists.'
print(ans)