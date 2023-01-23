import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
a = [tuple(map(int,input().split())) for i in range(K)]
x = {}
y = {}
for i,j in a:
    if i in x:
        x[i].append(j)
    else:
        x[i] = [j]
    if j in y:
        y[j].append(i)
    else:
        y[j] = [i]
A = []
B = []
for i in x:
    if len(x[i])%2:
        A.append(i)
for i in y:
    if len(y[i])%2:
        B.append(i)
print(max(len(A),len(B)))
flip = True
ans = []
if len(B)<len(A):
    A, B = B[:], A[:]
    flip = False
for j in B:
    if A:
        ans.append((A.pop(),j))
    else:
        ans.append((1,j))
        A.append(1)
for i in ans:
    if not flip:
        print(*i[::-1])
    else:
        print(*i)