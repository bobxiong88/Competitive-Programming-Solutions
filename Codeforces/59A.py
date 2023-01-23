s = input()
l = 0
u = 0
for i in s:
    if i.upper() == i:
        u += 1
    else:
        l += 1
if l >= u:
    print(s.lower())
else:
    print(s.upper())