import sys
input = sys.stdin.readline
L, H, W = map(int,input().split())
D = int(input())
r = D/2
print(L*H*W-r*r*3.1415*H)