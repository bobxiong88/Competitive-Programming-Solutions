import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int,input().split())
    if b >= 3:
        print("YES")
        print(a, a*(b-1), a*b)
    elif b == 2:
        print("YES")
        print(a*1,a*3, a*b*2)
    else:
        print("NO")
        
