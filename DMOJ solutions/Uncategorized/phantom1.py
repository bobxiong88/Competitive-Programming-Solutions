import sys
input = sys.stdin.readline
def prime(num):
    if num <= 1: return 0
    for x in range(2, int(num**0.5)+1):
        if num%x == 0: return 0
    return 1
for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    for i in range(a,b):
        ans += prime(i)
    print(ans)