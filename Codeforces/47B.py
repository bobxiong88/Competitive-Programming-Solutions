import sys
input = sys.stdin.readline
p = ['ABC','ACB','BAC','BCA','CAB','CBA']
for i in range(3):
    x = input().strip('\n')
    a = x[0]
    b = x[2]
    if x[1] == '<':
        a,b = b,a
    fap = []
    for o in p:
        if o.index(a) < o.index(b):
            fap.append(o)
    for o in fap: p.remove(o)
if p:
    print(p[0])
else:
    print('Impossible')
