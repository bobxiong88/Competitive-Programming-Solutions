import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for i in range(N)]
psa = [0]
for i in range(N): psa.append(arr[i]+psa[-1])
Q = int(input())
for i in range(Q):
    x,y = map(int,input().split())
    x+=1
    y+=1
    print(psa[y]-psa[x-1])