from math import ceil
N, B, S, G = map(int,input().split())
K = B+S*3+G*5
if N < K:
    print(0)
else:
    diff = N-K+1
    print(diff//5+((diff%5)!=0))