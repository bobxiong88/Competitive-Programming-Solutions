import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, t = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    ans = [0 for i in range(n)]
    for i in range(n):
        if a[i]>t/2:
            ans[i] = 1
        elif a[i] == t/2:
            l^=1
            ans[i] = l
    print(*ans)
'''
11 7
1 1 2 3 4 5 5 6 7 9 9

'''
