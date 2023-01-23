import sys
input = sys.stdin.readline
N = int(input())
res = 1
c = 0
for i in range(1,N+1):
    res *= i
    while res >= 10:
        res /= 10
        c+=1
res=round(res,10)
print("{}e+{}".format(res,c))