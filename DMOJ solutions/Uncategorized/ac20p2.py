import sys
input = sys.stdin.readline
from math import *
freq = [0]*int(1e5+1)
N, Q = map(int,input().split())
a = list(map(int,input().split()))
for i in a:
    freq[i]+=1
for i in range(Q):
    q,x = map(int,input().split())
    if q == 1:
        n = freq[x]
        freq[x] = 0
        freq[ceil(x/2)] += n
        freq[floor(x/2)] += n
    else:
        print(freq[x])