N = int(input())
pos = sorted([tuple(map(int,input().split())) for i in range(N)])
print(max([abs((pos[i][1]-pos[i+1][1])/(pos[i][0]-pos[i+1][0])) for i in range(N-1)]))