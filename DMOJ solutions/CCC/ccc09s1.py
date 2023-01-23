import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = 0
for i in range(round(a**(1/3)), round(b**(1/3))+1):
    if abs(i**1.5-int(i**1.5))<0.000001:
        c+=1
print(c)