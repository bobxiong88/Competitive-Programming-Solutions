def dp(coins, m, V):
    values = [float('inf') for i in range(V+1)]
    values[0]=  0
    for x in range(1,V+1):
        for y in range(m):
            if coins[y]<=x:
                
                result = values[x-coins[y]]
                if result!=float('inf') and result+1<values[x]:
                    values[x] = result+1
    return values[V]
V = int(input())
m = int(input())
clubs = []
for i in range(m):
    clubs.append(int(input()))

val = dp(clubs,m, V)
if val == float('inf'):
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in",val,"strokes.")