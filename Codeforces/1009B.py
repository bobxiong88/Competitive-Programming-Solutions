import sys
input = sys.stdin.readline
s = input().strip('\n')
b = []
c = 0
last = -1
for i in range(len(s)):
    if s[i]=='1':
        c+=1
    else:
        b.append(s[i])
        if s[i] == '2' and last == -1:
            last = len(b)-1
if last!=-1:
    b = ''.join(b[:last])+'1'*c+''.join(b[last:])
else:
    b = ''.join(b)+'1'*c
print(b)
