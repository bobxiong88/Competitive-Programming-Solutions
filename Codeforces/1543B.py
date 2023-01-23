import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    r = s%n
    x = (s-r)//n
    print(r*(n-r))
    
    
    
