import sys
input = sys.stdin.readline
N = int(input())
name, score = "", -1
for i in range(N):
    a,b = map(str,input().split())
    b = float(b)
    if b>score:
        name,score = a,b
print(name)