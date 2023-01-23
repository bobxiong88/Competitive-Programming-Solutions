import sys
input = sys.stdin.readline
def f(x):
    cnt = 0
    while x%2 == 0:
        x//=2
        cnt+=1
    return cnt
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a = [f(i) for i in a]
    if min(a) == 0:
        print(n-a.count(0))
    else:
        print(min(a)+n-1)
