import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    j = n-1
    a,b = 0,0
    ca,cb = 0,0
    m = 0
    while True:
        ca = 0
        while ca<=cb and i<=j:
            ca += arr[i]
            i+=1
        a+=ca
        m+=1
        if i>j:
            break
        cb = 0
        while cb<=ca and i<=j:
            cb += arr[j]
            j-=1
        b+=cb
        m+=1
        if i>j:
            break
    print(m,a,b)
