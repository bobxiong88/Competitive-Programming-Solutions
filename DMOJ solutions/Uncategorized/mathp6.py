# fix value of d,  -sqrt(M)<= d <= sqrt(M)
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
delta = 4*(N**2)-16*(N**2-3*M)
if delta < 0:
    print("no")
    sys.exit(0)
print((2*N+delta**0.5)/8)