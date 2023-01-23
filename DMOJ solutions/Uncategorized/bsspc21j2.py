import sys
input = sys.stdin.readline
M = int(input())
c = [tuple(map(int,input().split())) for i in range(M)]
for i in range(int(input())):
    a, b = map(int,input().split())
    game = False
    for x, y in c:
        if b>=x and a <=y:
            game = True
            break
    if game:
        print("Break is Over! Stop playing games! Stop watching Youtube!")
    else:
        print(":eyy:")