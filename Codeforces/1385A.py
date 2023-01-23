import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    a,b,c = 0,0,0
    if x==y and x>z:
        a = x
        b = z
        c = z
    elif x==z and x>y:
        b = z
        a = y
        c = y
    elif y==z and y>x:
        c = y
        b = x
        a = x
    elif x==y==z:
        a,b,c = x,y,z
    if not any((a,b,c)):
        print("NO")
    else:
        print("YES")
        print(a,b,c)
        
