import sys
#11:02
sys.setrecursionlimit(1000000)
a = int(input())
b = int(input())

graph = dict()
for i in range(a):
    row = list(map(int,input().split()))
    for j,value in enumerate(row):
        if not i and not j:
            start = value
        mapped = (i+1)*(j+1)
        try:
            graph[value].append(mapped)
        except:
            graph[value]=[mapped]
possible = []
visited = set()

def dfs(x):
    for i in graph[x]:
        if i in visited: continue
        if i not in graph: continue
        if(start==i):
            print("yes")
            sys.exit(0)
        visited.add(i)
        dfs(i)
if a*b == start:
    print("yes")
    sys.exit(0)

if a*b in graph:
    dfs(a*b)

print("no")