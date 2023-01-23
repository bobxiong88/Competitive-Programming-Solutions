s = input()
l = 0
u = 0
for i in s:
    if i == ' ': continue
    elif i.upper() == i:
        u += 1
    else:
        l += 1
if l > u:
    print(s.lower())
elif l == u:
    print(s)
else:
    print(s.upper())