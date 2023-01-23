import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for i in range(N):
    a = int(input())
    b = int(input())
    if a*5-b*3>40:
        cnt+=1
out = str(cnt)
if cnt == N: out = out + "+"
print(out)