import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    if k<=n and (n-(k-1))%2==1:
        print("YES")
        out = [1 for i in range(k-1)]+[n-(k-1)]
        print(*out)
    elif (n-(k-1)*2)>0 and (n-(k-1)*2)%2==0:
        print("YES")
        out = [2 for i in range(k-1)]+[n-(k-1)*2]
        print(*out)
    else:
        print("NO")
