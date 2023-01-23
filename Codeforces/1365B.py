import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if (b.count(0)==n or b.count(1)==n) and sorted(a)!=a:
        print("No")
    else:
        print("Yes")
