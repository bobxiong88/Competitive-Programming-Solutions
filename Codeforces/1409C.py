import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,x,y = map(int,input().split())
    diff = y-x
    div = []
    for i in range(1,diff+1):
        if diff%i==0:
            if diff//i+1<=n:
                div.append(i)
    arr = []
    for i in range(1,x+1):
        for fac in div:
            if (x-i)%fac==0 and (y-i)%fac==0:
                arr.append([fac*j+i for j in range(n)])
    ans = []
    mn = float('inf')
    for a in arr:
        if max(a)<mn and max(a)>=y:
            ans = a
            mn = max(a)
    print(*ans)
