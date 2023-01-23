import sys
input = sys.stdin.readline
def num(n):
    return 9*10**((n-1)//2)
N = int(input())
if N>20:
    print(999999998)
else:
    s = 0
    for i in range(1,N+1):
        s += num(i)
    print(s%1000000000)