import math
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
for i in range(5):
    R = int(input())
    m = int(input())
    rocks = []
    for i in range(R):
        rocks.append(tuple(map(int,input().split())))
    rocks = convex_hull(rocks)
    cost = 0
    for i in range(len(rocks)):
        a,b = rocks[i-1]
        x,y = rocks[i]
        cost += math.ceil(((a-x)**2 + (b-y)**2)**0.5)*m
    print("$"+str(cost)+".00")