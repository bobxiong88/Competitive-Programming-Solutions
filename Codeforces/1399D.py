import sys
input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    n = int(input())
    s = [int(i) for i in input()[:n]]
    ans = []
    c = 0
    
    d = [[],[]]
    for i in s:
        x = 1-i
        if len(d[x])>0:
            peepee = d[x].pop()
            d[i].append(peepee)
        else:
            c+=1
            d[i].append(c)
            peepee = c
        ans.append(peepee)
    print(max(ans))
    print(*ans)
'''
10
10
0010100101
'''
