import sys
input = sys.stdin.readline
N = int(input())
points = {}
for i in range(N):
    x,y = map(int,input().split())
    try:
        points[x].append(y)
    except:
        points.update({x:[y]})
area = 0
for key in points.keys():
    for a in points[key]:
        for b in points[key]:
            if a!=b:
                for x in points.keys():
                    if a in points[x] and b in points[x]:
                        area = max(area, abs(a-b)*abs(key-x))
print(area)