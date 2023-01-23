import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0
f = False
blocks = []
for i in range(N):
    if f:
        if not B[i]:
            blocks.append((a,b))
            f = False
        else:
            b = i
    elif B[i]:
        a = i
        b = i
        f = True
if f: blocks.append((a,b))
blocks = blocks[::-1]
i = N-1
ops = []
for a, b in blocks:
    x = 0
    i = min(i, b)
    init = i
    while i!= -1 and x < b-a+1:
        x += A[i]
        i -= 1
    if all([A[j] == B[j] for j in range(a,b+1)]): continue
    for j in range(i+1, init+1):
        A[j] = 0
    for j in range(b-x+1, b+1):
        A[j] = 1
    ops.append((i+1,b))
if not all([A[i]==B[i] for i in range(N)]):
    print(-1)
    sys.exit(0)
print(len(ops))
for a, b in ops:
    print(a+1, b+1)