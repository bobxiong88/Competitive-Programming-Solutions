import sys
input = sys.stdin.readline
MOD = int(1e9) + 7
def fib(n):
    v1, v2, v3 = 1, 1, 0   
    for rec in bin(n)[3:]:  
        calc = v2*v2
        v1, v2, v3 = (v1*v1+calc)%MOD, ((v1+v3)*v2)%MOD, (calc+v3*v3)%MOD
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2

n = int(input())

print(fib(n))