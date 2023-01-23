n = int(input())
c = 0
for i in range(n):
    if i<=n-i and n-i<=5:c+=1
print(c)