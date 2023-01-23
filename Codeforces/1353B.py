import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    i = 0
    j = n-1
    for x in range(k):
        if b[j]>a[i]:
            a[i] = b[j]
            j-=1
            i+=1
    print(sum(a))
