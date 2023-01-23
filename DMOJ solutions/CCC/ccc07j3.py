import sys
input = sys.stdin.readline
a = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
n = int(input())
b = [int(input()) for i in range(n)]
s = 0
for i in range(10):
    if i+1 not in b: s += a[i]
x = int(input())
if x > s/(10-n): print("deal")
else: print("no deal")