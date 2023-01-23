s = input()
v = s.count('V')
h = s.count('H')
a = [[1,2],[3,4]]
if h%2: a = a[::-1]
if v%2: a[0][0], a[0][1], a[1][0], a[1][1] = a[0][1], a[0][0], a[1][1], a[1][0]
for i in a: print(*i)