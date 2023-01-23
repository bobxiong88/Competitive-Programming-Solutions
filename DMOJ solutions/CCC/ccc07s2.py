import sys
input = sys.stdin.readline
n = int(input())
boxes = [sorted(list(map(int,input().split()))) for i in range(n)]
m = int(input())
for i in range(m):
    ans = float('inf')
    x,y,z = map(int,input().split())
    x,y,z = sorted([x,y,z])
    for a,b,c in boxes:
        if x<=a and y<=b and z<=c:
            ans = min(ans, a*b*c)
    if ans == float('inf'): ans = "Item does not fit."
    print(ans)