import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    even = []
    odd = []
    for i in range(n):
        if a[i]%2==0:
            even.append(i)
        else:
            odd.append(i)
    if even:
        print(1)
        print(even[0]+1)
        continue
    else:
        if len(odd)>=2:
            print(2)
            print(odd[0]+1,odd[1]+1)
            continue
    print(-1)
