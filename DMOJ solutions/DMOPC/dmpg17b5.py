import sys
input = sys.stdin.readline
N = int(input())
time = [0 for i in range(1000005)]
for i in range(N):
    a,b = map(int,input().split())
    time[a] = max(time[a], b)
for i in range(1,1000005):
    time[i] = max(time[i],time[i-1])
Q = int(input())
for i in range(Q):
    T = int(input())
    print(time[T])