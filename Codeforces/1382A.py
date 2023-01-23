import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = tuple(map(int,input().split()))
    b = tuple(map(int,input().split()))
    ans = float('inf')
    for i in a:
        if i in b:
            print("YES")
            ans = i
            print(1,i)
            break
    if ans == float('inf'):
        print("NO")
