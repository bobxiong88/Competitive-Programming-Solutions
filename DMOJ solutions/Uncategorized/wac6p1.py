import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    p,c = map(float,input().split())
    print(p/(c+100)*100)