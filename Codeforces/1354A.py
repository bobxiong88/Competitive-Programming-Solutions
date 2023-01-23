import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a,b,c,d = map(int,input().split())
    if b>=a:
        print(b)
        continue
    a-=b
    time = c-d
    if time<=0:
        print(-1)
        continue
    print(math.ceil(a/time)*c+b)
    
