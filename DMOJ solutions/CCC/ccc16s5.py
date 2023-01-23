import sys
input = sys.stdin.readline
N, T = map(int,input().split())
last = list(map(int,input().strip('\n')))
ans = [0]*N
T = list(map(int,bin(T)[2:]))[::-1]
for x in range(len(T)):
    if T[x]:
        curr = [0]*N
        for i in range(N):
            curr[i] = last[(i-2**x)%N]^last[(i+2**x)%N]
        last = curr[:]
print(''.join([str(i) for i in last]))