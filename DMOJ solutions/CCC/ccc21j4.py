import sys
input = sys.stdin.readline
s = list(input().strip('\n'))
n = len(s)
cl = s.count('L')
cm = s.count('M')
L, M, S = [], [], []
for i in range(n):
    if i>cl-1:
        if s[i] == 'L': L.append(i)
    else:
        if s[i] == 'M': M.append(i)
        elif s[i] == 'S': S.append(i)
ans = len(L)
for i in S:
    j = L.pop()
    s[i], s[j] = s[j], s[i]
for i in M:
    j = L.pop()
    s[i], s[j] = s[j], s[i]
for i in range(cl, cl+cm):
    if s[i] == 'S':
        ans += 1
print(ans)