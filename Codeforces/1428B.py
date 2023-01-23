import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = input().strip('\n')
    graph = [[] for i in range(n)]
    if '>' not in a or '<' not in a:
        print(n)
        continue
    ans = 0
    for i in range(n):
        if a[i] == '-' or a[i-1] == '-':
            ans+=1
    print(ans)
