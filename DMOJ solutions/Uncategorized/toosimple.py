n = True+True
s = str()
ans = False
for x, i in enumerate([False,False,False,True,False,False,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([True,False,True,False,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,False,True,True,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,False,True,True,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([True,True,True,True,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,False,True,True,False,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,False,False,False,False,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([True,True,True,False,True,False,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([True,True,True,True,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,True,False,False,True,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,False,True,True,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([False,False,True,False,False,True,True]):
    ans += i*n**x
s += chr(ans)
ans = False
for x, i in enumerate([True,False,False,False,False,True]):
    ans += i*n**x
s += chr(ans)
print(s)