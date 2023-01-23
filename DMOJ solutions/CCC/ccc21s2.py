import sys
input = sys.stdin.readline
M, N, K = [int(input()) for i in range(3)]
row = [0]*M
col = [0]*N
for i in range(K):
    q,x = input().split()
    x = int(x)-1
    if q == 'R': row[x] ^= 1
    else: col[x] ^= 1
A = col.count(1)
B = row.count(1)
print(A*M+B*N-2*A*B)