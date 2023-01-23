import sys
input = sys.stdin.readline
a = [int(input()) for i in range(4)]
u, d, c = 0, 0 ,0
for i in range(3):
    if a[i]>a[i+1]: d+=1
    elif a[i]<a[i+1]: u+=1
    else: c+=1
if u==3: print('Fish Rising')
elif d==3: print('Fish Diving')
elif c==3: print('Fish At Constant Depth')
else: print('No Fish')