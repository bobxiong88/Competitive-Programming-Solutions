import sys
input = sys.stdin.readline
T = int(input())
def p(top, bottom, i, j, n):
    while top!=1 or bottom!=n:
        if a[i] == top-1:
            top = a[i]
            i+=1
        elif a[i] == bottom+1:
            bottom = a[i]
            i+=1
        elif a[j] == top-1:
            top = a[j]
            j-=1
        elif a[j] == bottom+1:
            bottom = a[j]
            j-=1
        else:
            return False
    return True
for t in range(1, T+1):
    n = int(input())
    a = list(map(int,input().split()))
    if n<=3:
        print("Case #"+str(t)+": yes")
        continue
    ans = 'no'
    if p(a[0],a[0], 1, n-1,n) or p(a[n-1],a[n-1],0,n-2,n):
        ans = 'yes'
    print("Case #"+str(t)+": "+ans)