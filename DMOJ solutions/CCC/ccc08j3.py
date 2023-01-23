lol = ['ABCDEF','GHIJKL','MNOPQR','STUVWX','YZ -.']
s = input()
x, y = 0, 0
ans = 0
for i in s:
    for j in range(5):
        if i in lol[j]:
            ans += abs(x-lol[j].index(i))+abs(y-j)
            x = lol[j].index(i)
            y = j
            break
ans += abs(x-5)+abs(y-4)
print(ans)