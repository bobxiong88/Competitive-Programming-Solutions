import sys
from math import log
input = sys.stdin.readline
n,a,b = map(int,input().split())
x = [[i] for i in range(1,n+1)]
for i in range(int(log(n,2))):
    for z in x:
        if a in z and b in z:
            print(i)
            sys.exit(0)
    new = []
    for k in range(0,len(x)//2):
        new.append(x[k*2]+x[k*2+1])
    x = new[:]
print("Final!")
