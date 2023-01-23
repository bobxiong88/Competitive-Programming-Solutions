import sys
from math import log
from math import factorial as f
from math import ceil
input = sys.stdin.readline
def bino(a,b): return int(f(a)/(f(b)*f(a-b)))
def b(a): return bin(a)[2:]
n = int(input())
ans = 0
for i in range(1,int(log(n,2))+1):
    k = (i+1)//2 - 1
    for j in range(1,k+1):
        ans += bino(i, j)
    ans += 1
for i in range(n+1, 2**(int(log(n,2))+1)):
    a = b(i)
    if a.count('0') >= ceil(len(a)/2):
        ans-=1

'''
for j in range(2**(i+1), n+1):
    a = b(j)
    if a.count('0') >= ceil(len(a)/2):
        ans+=1
'''
'''
a = b(n)
for i in range(1, int(log(n,2))+1):
    if a[i] == '1':
        k = len(a)//2-1
        for j in range(1,k+1):
            ans += bino(len(a)-i-1, j)
        break
'''
print("There are {} round numbers less than or equal to {}.".format(ans, n))