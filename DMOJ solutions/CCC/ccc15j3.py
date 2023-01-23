import sys
input = sys.stdin.readline
a = list(input().strip('\n'))
d = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(a)):
    if a[i] not in 'aeiou':
        s = a[i]
        c = float('inf')
        l = ''
        for k in 'aeiou':
            if abs(d.index(k)-d.index(a[i])) < c:
                c = abs(d.index(k)-d.index(a[i]))
                l = k
        s = s + l
        c = 'z'
        for k in d[d.index(a[i])+1:]:
            if k not in 'aeiou':
                c = k
                break
        s = s + c
        a[i] = s
print(''.join(a))