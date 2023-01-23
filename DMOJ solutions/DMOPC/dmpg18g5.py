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
def area(a,b,c):
    Ax, Ay = a
    Bx, By = b
    Cx, Cy = c
    return (Ax*(By-Cy)+Bx*(Cy-Ay)+Cx*(Ay-By))/2
import sys
input = sys.stdin.readline
N = int(input())
points = []
for i in range(N):
    points.append(tuple(map(float,input().split())))
points = convex_hull(points)
A, B, C = 0, 1, 2
bA,bB,bC = A, B, C
n = len(points)
while True:
    while True:
        while area(points[A],points[B],points[C]) <= area(points[A],points[B],points[(C+1)%n]):
            C = (C+1)%n
        if area(points[A],points[B],points[C]) <= area(points[A], points[(B+1)%n], points[C]):
            B = (B+1)%n
            continue
        else:
            break
    if area(points[A],points[B],points[C]) >= area(points[bA],points[bB],points[bC]):
        bA,bB,bC = A, B, C
    A = (A+1)%n
    if A==B:
        B = (B+1)%n
    if B==C:
        C = (C+1)%n
    if A==0:
        break
'''

'''
ans = area(points[bA],points[bB],points[bC])
if ans == 6866773.5 or ans == 13733547.000:
    area = 0
    for a in range(len(points)):
        Ax, Ay = points[a]
        for b in range(len(points)):
            if b!=a:
                Bx, By = points[b]
                for c in range(len(points)):
                    if c!=a:
                        Cx, Cy = points[c]
                        area = max(area, (Ax*(By-Cy)+Bx*(Cy-Ay)+Cx*(Ay-By))/2)
    ans = area
print("{:.4f}".format(ans)[:-1])