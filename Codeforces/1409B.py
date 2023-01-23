import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,x,y,n = map(int,input().split())
    save = [a,b,x,y,n]
    a,b,x,y = b,a,y,x
    if (b-n)>=y:
        b-=n
    else:
        n-=(b-y)
        b=y
        a = max(a-n, x)
    ans = b*a
    
    a,b,x,y,n =  save
    if (b-n)>=y:
        b-=n
    else:
        n-=(b-y)
        b=y
        a = max(a-n, x)
    ans = min(ans,b*a)
    print(ans)
        
