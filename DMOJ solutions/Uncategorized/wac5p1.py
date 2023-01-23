import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort()
s = 0
queue = deque(a)
while queue:
    sub = []
    newQueue = []
    while queue:
        curr = queue.popleft()
        if sub:
            if curr>sub[-1]:
                sub.append(curr)
            else:
                newQueue.append(curr)
        else:
            sub.append(curr)
    s+=sub[-1]
    queue = deque(newQueue)
print(s)