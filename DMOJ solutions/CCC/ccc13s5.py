import sys
input = sys.stdin.readline
c = 0
n = int(input())
while True:
    if n==1: break
    for i in xrange(int(n/2), n):
        if i%(n-i)==0:
            c+=i//(n-i)
            n = i
            break
print(c)