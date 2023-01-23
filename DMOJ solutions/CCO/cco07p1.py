# thank you wikipedia, pls no ban i am just learning convex hull
def convex_hull(points):

    points = sorted(set(points))

    if len(points) <= 1:
        return points


    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)


    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

n = int(input())
points = []

for i in range(n):
    a,b = map(int,input().split())

    points.append((a+1000,b+1000))

points = convex_hull(points)
total = 0
for i in range(len(points)):
    x1,y1 = points[i-1]
    x2,y2 = points[i]
    total+= x1*y2 - x2*y1
total = abs(total)/2
print(int(total//50))