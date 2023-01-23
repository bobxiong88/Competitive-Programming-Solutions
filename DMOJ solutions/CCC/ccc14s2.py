import sys
input = sys.stdin.readline
n = int(input())
a = input().strip('\n').split()
b = input().strip('\n').split()
d = {}
for i in range(n):
    x,y = a[i],b[i]
    if x in d: d[x].add(y)
    else: d.update({x:{y}})
    if y in d: d[y].add(x)
    else: d.update({y:{x}})
c = True
for i in d:
    if len(d[i])!=1 or i in d[i]:
        c = False
        break
print('good' if c else 'bad')