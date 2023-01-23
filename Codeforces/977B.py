import sys
input = sys.stdin.readline
n = int(input())
s = input()[:n]
mx = 0
m = ''
letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
p = []
for i in range(26):
    for j in range(26):
        p.append(letters[i]+letters[j])
for i in p:
    c = 0
    for j in range(n-1):
        if s[j]==i[0] and s[j+1]==i[1]: c+=1
    if c>mx:
        mx = c
        m = i
print(m)
