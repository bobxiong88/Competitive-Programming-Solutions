from collections import deque 

M = int(input())

arr = [[] for i in range(M+1)]
for i in range(M):
  X, Y = map(int, input().split())
  arr[X].append(Y)
A, B = map(int, input().split())
def bfs(arr, A, B):
  visited = [False] * (M+1)
  visited[A] = True
  queue = deque([A])

  if A == B:
    return("if same")

  while queue:
    node = queue.popleft()
    for i in arr[node]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        if i == B:
          return("they are connected")
  return None

if bfs(arr, A, B):
  print("Tangled")
else:
  print("Not Tangled")