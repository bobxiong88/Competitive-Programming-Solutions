import sys
input = sys.stdin.readline
m = 10**9+7
n = input().strip('\n')
a = [int(i) for i in n]
n = len(n)
table = []
s = 0
for i in range(n):
    s = (s+(i+1)*pow(10,i,m))%m
    table.append(s)
s = 0
for i in range(n):
    x = n-i-2
    if x>=0:
        s += a[i]*table[x]
    s += (i*(i+1)//2)*a[i]*pow(10,x+1,m)
    s = s%m
print(s)
