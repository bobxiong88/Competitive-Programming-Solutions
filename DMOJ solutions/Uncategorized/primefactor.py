import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    a = int(input())
    i = 2
    f = []
    while i**2 <= a and a!=1:
        if a%i == 0:
            a//=i
            f.append(i)
        else:
            i+=1
    if a != 1:
        f.append(a)
    print(' '.join([str(i) for i in f]))