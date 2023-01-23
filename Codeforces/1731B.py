import sys
input  = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = (n*(4*n-1)*(n+1))//6
    s = s*2022
    s = s%(int(1e9)+7)
    print(s)
