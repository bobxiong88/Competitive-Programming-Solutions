import sys
input = sys.stdin.readline
S, R = map(int,input().split())
if S**2 > 3.14*(R**2):
    print("SQUARE")
else:
    print("CIRCLE")