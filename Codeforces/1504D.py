import sys
input = sys.stdin.readline
n = int(input())
black = []
white = []
grid = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        k = (i+j)%2
        if k:
            black.append((i+1,j+1))
        else:
            white.append((i+1,j+1))
for i in range(n):
    for j in range(n):
        a = int(input())
        if a == 1:
            if white:
                print(2, *white.pop())
            else:
                print(3, *black.pop())
        elif a == 2:
            if black:
                print(1, *black.pop())
            else:
                print(3, *white.pop())
        else:
            if black:
                print(1, *black.pop())
            else:
                print(2, *white.pop())
        sys.stdout.flush()
