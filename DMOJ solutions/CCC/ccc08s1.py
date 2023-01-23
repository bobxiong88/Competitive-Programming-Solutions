a = []
while True:
    c, t = input().split()
    a.append((c, int(t)))
    if c=='Waterloo': break
a.sort(key = lambda x: x[1])
print(a[0][0])