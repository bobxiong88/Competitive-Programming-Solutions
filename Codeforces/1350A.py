import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    while k:
        for i in range(2,n+1):
            if n%i==0:
                n+=i
                break
        k-=1
        if n%2==0:
            break
    n+=k*2
    print(n)
