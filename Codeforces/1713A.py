import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    xs = [0]
    ys = [0]
    for i in range(n):
        x, y = map(int,input().split())
        xs.append(x)
        ys.append(y)
    print((max(xs)-min(xs)+max(ys)-min(ys))*2)
