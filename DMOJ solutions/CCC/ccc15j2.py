s = input().strip('\n')
a, b = 0, 0
for i in range(len(s)-2):
    if s[i:i+3]==':-)': a+=1
    elif s[i:i+3]==':-(': b+=1
if a==b==0: print('none')
elif a>b: print('happy')
elif a<b: print('sad')
else: print('unsure')