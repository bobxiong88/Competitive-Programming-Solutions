s = input()
k = 'BFTLC'
m = True
for i in k:
    if i not in s:
        print(i)
        m = False
if m: print("NO MISSING PARTS")