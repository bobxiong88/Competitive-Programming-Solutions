import sys
input = sys.stdin.readline
s = input().strip('\n')
n = len(s)
l,o,v,e = [0]*4
for i in range(-1, -n-1, -1):
    if s[i] == 'e': e+=1
    elif s[i] == 'v': v+=e
    elif s[i] == 'o': o+=v
    elif s[i] == 'l': l+=o
print(l)