import sys
input = sys.stdin.readline
def bn(a):
    return bin(a)[2:]
for _ in range(int(input())):
    a,b = map(int,input().split())
    if b<a:
        a,b = b,a
    print(a^b)
