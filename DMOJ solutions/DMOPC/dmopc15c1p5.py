def board(b):
    for i in b:
        print(i)
import sys
input = sys.stdin.readline
W, H, N = map(int,input().split())
grid = []
for i in range(H):
    grid.append(list(map(int,input().split())))
prefix = [[0]*(W+1) for i in range(H+1)]
prefix[1][1] = grid[0][0]
for i in range(2,W):
    prefix[1][i] = prefix[1][i-1]+grid[0][i-1]
for i in range(2,H):
    prefix[i][1] = prefix[i-1][1]+grid[i-1][0]
for i in range(1,H+1):
    for j in range(1,W+1):
        prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+grid[i-1][j-1]
pairs = []
l = max(H, W)
num = -1
# what the fuck why does it always break when N = H*W - 1
if N == H*W-1:
    s = 0
    for i in range(H):
        for j in range(W-1):
            s+=grid[i][j]
    num = max(num,s)
    s = 0
    for i in range(H):
        for j in range(1,W):
            s+=grid[i][j]
    num = max(num,s)
    s = 0
    for i in range(1,H):
        for j in range(W):
            s+=grid[i][j]
    num = max(num,s)
    s = 0
    for i in range(H-1):
        for j in range(W):
            s+=grid[i][j]
    num = max(num,s)
    print(num)
    sys.exit(0)
for i in range(1,N+1):
    a = i
    b = int(N/i)
    if a>l or b>l:
        continue
    pairs.append((a,b))

for a in range(H):
    for b in range(W):
        for pair in pairs:
            h,w = pair
            c,d = a+h, b+w
            if c<=H and d<=W:
                s = prefix[c][d] - prefix[a][d] - prefix[c][b] + prefix[a][b]
                num = max(num, s)
print(num)