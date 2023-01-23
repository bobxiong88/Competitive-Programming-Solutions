import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x,n,m = map(int,input().split())
    while True:
        s = int(str(x))
        if x>=21 and n>=1:
            n-=1
            x = x//2+10
        elif m>=1:
            m-=1
            x-=10
        if not n and not m:
            break
        if x<=0:
            break
        if s==x:
            break
    if x>0:
        print("NO")
    else:
        print("YES")
