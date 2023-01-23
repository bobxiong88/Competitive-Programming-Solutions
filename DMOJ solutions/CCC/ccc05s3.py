import sys
input = sys.stdin.readline
n = int(input())
a = []
def gay(board):
    for i in board: print(i)
for i in range(n):
    r,c = map(int,input().split())
    curr = [list(map(int,input().split())) for i in range(r)]
    if not i:
        a = curr[:]
        continue
    m,n = len(a),len(a[0])
    temp = [[] for i in range(m*r)]
    for x in range(m):
        row = []
        for y in range(n):
            new = [[] for i in range(r)]
            for i in range(r):
                for j in range(c):
                    new[i].append(curr[i][j]*a[x][y])
            row.append(new)
        for i in range(r):
            for j in range(n):
                temp[x*r+i] = temp[x*r+i]+row[j][i]
    a = temp[:]
m,n = len(a),len(a[0])
q1 = -float('inf')
q2 = float('inf')
q3 = -float('inf')
q4 = float('inf')
q5 = -float('inf')
q6 = float('inf')
for i in range(m):
    q1 = max(q1,max(a[i]))
    q2 = min(q2,min(a[i]))
    q3 = max(q3,sum(a[i]))
    q4 = min(q4,sum(a[i]))
for j in range(n):
    c = 0
    for i in range(m): c+=a[i][j]
    q5 = max(q5,c)
    q6 = min(q6,c)
print("{}\n{}\n{}\n{}\n{}\n{}".format(q1,q2,q3,q4,q5,q6))