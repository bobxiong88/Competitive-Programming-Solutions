import sys
input = sys.stdin.readline
def win(state, record):
    if not state:
        for i in range(1,5):
            if i!=t:
                if record[t]<=record[i]:
                    return 0
        return 1
    a,b = state.pop(0)
    n1 = record[:]
    n1[a]+=3
    n2 = record[:]
    n2[b]+=3
    n3 = record[:]
    n3[a]+=1
    n3[b]+=1
    return win(state[:], n1) + win(state[:], n2) + win(state[:], n3)
t = int(input())
g = int(input())
score = [0]*5
vis = [[False]*5 for i in range(5)]
for i in range(g):
    a,b,sa,sb = map(int,input().split())
    vis[a][b] = True
    if sa>sb: score[a]+=3
    elif sa<sb: score[b]+=3
    else: score[a], score[b] = score[a]+1, score[b]+1
pos = []
for i in range(1,5):
    for j in range(i+1,5):
        if not vis[i][j]:
            pos.append((i,j))
print(win(pos, score))