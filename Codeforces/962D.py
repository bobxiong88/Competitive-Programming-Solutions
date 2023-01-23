# size of array decreases by 1 each time, we can just simulate
# maintain priority queue on position for each value, merge from smallest to largest
# push result into array, sort then print

from heapq import *
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
vals = []
heapify(vals)
pos = dict()
for i in range(n):
    if a[i] in pos:
        heappush(pos[a[i]], i)
    else:
        pos[a[i]] = [i]
        heapify(pos[a[i]])
        heappush(vals, a[i])
while vals:
    num = heappop(vals)
    while len(pos[num]) >= 2:
        a = heappop(pos[num])
        b = heappop(pos[num])
        if num*2 in pos:
            heappush(pos[num*2], b)
        else:
            pos[num*2] = [b]
            heapify(pos[num*2])
            heappush(vals, num*2)
withpos = []
for i in pos.keys():
    for j in pos[i]:
        withpos.append((j, i))
withpos.sort()
print(len(withpos))
print(*[i[1] for i in withpos])
