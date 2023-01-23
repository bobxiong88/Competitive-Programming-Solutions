import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    ans = 0
    pre = []
    mx = -1
    for i in range(n):
        mx = max(mx, b[i])
        pre.append(mx)
    for i in range(n):
        if b[i]<pre[i]:
            if b[i]<b[i-1]:
                ans+=b[i-1]-b[i]
    print(ans)
'''
15
3 1 4 1 5 3 2 7 4 5 3 9 6 3 4

11
3 1 4 1 5 9 2 6 5 7 9

9
2 7 1 8 2 3 5 4 3
'''
