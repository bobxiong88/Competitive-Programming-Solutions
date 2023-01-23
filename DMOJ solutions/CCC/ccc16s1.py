a = input()
b = input()
ans = 'A'
for i in 'abcdefghijklmnopqrstuvwxyz':
    if a.count(i)<b.count(i):
        ans = 'N'
        break
print(ans)