import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    a.sort()
    for i in range(1,n+1):
        if a[i-1]<=i:
            ans = i
    
    print(ans+1)
    #print(a)
