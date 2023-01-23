import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip('\n')
    res = 0
    for i in s:
        res = max(res, ord(i))
    print(res-ord('a')+1)
