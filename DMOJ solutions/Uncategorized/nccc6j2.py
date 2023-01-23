s = input()
ans = 0
k = 'pusheen'
for i in range(7):
    if s[i]!=k[i]: ans += 1
print(ans)