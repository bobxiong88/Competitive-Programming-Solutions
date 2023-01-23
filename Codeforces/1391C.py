import sys
input = sys.stdin.readline
n = int(input())
mod = 1000000000+7
def fac(n, modulus):
    ans=1
    if n <= modulus//2:
        #calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1,n+1):
            ans = (ans * i) % modulus   
    else:
        #Fancypants method for large n
        for i in range(n+1,modulus):
            ans = (ans * i) % modulus
        ans = modinv(ans, modulus)
        ans = -1*ans + modulus
    return ans % modulus
a = 1
for i in range(1,n):
    a = (a*2)%mod
print((fac(n,mod)-a)%mod)
