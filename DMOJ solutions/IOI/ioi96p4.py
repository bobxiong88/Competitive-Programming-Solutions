import sys
input = sys.stdin.readline
n = int(input())
s = [int(input()) for i in range(n)]
cl = s.count(1)
cm = s.count(2)
swap = []
lis = []
L, M, S = [], [], []
for i in range(n):
    if i>cl-1:
        if s[i] == 1: L.append(i)
    else:
        if s[i] == 2: M.append(i)
        elif s[i] == 3: S.append(i)
for i in S:
    j = L.pop()
    s[i], s[j] = s[j], s[i]
    swap.append((i,j))
for i in M:
    j = L.pop()
    s[i], s[j] = s[j], s[i]
    swap.append((i,j))
for i in range(cl+cm,n):
    if s[i] == 2:
        lis.append(i)
for i in range(cl, cl+cm):
    if s[i] == 3:
        swap.append((i,lis.pop()))
print(len(swap))
for a,b in swap: print(a+1,b+1)