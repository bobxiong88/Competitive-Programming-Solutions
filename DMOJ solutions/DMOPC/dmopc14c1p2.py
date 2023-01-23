a,b = map(int,input().split())
n = int(input())
a -= a%n
b -= b%n
print(a*b//n**2)