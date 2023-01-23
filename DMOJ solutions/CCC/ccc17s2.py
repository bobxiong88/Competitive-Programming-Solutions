from math import *
n = int(input())
a = list(map(int,input().split()))
a.sort()
low = a[:ceil(n/2)]
low = low[::-1]
high = a[ceil(n/2):]
x,y = 0, 0
ans = []
for i in range(n):
    if not i%2:
        ans.append(low[x])
        x+=1
    else:
        ans.append(high[y])
        y+=1
print(*ans)