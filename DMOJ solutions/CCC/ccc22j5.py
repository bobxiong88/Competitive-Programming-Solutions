import sys
input = sys.stdin.readline
def can_place(size):
    global N
    global T
    for i in range(T):
        for j in range(i+1, T):
            x1,y1 = trees[i]
            x2,y2 = trees[j]
            xs = [0,N+1]
            ys = [0,N+1]
            for x, y in trees:
                if min(x1, x2) < x < max(x1, x2):
                    ys.append(y)
                if min(y1, y2) < y < max(y1, y2):
                    xs.append(x)
            xs.sort()
            ys.sort()
            if max(y1,y2) - min(y1, y2)-1 >= size:
                for k in range(len(xs)-1):
                    if xs[k+1]-xs[k] > size:
                        #print("straiught")
                        return True
            if max(x1,x2) - min(x1, x2)-1 >= size:
                for k in range(len(ys)-1):
                    if ys[k+1]-ys[k] > size:
                        #print("gay", ys, size)
                        return True
    a = [(1,1,size,size), (1,N-size+1,size,N), (N-size+1, 1, N, size), (N-size+1, N-size+1, N, N)] #x1,y1,x2,y2
    for x1,y1, x2,y2 in a:
        cond = True
        for x, y in trees:
            cond = cond and not(x1 <= x <= x2 and y1 <= y <= y2)
        if cond: return True
    return False
N = int(input())
T = int(input())
trees = [tuple(map(int,input().split())) for i in range(T)]
l = 0
r = N
ans = 0
while l <= r:
    m = (l+r)//2
    if can_place(m):
        l = m+1
        ans = m
    else:
        r = m-1
print(ans)