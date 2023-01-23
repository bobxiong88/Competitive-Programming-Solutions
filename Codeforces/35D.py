import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')
n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    a[i] = a[i]*(n-i)
a.sort()
s = 0
for i in range(n):
    s += a[i]
    if s > x:
        break
if s<=x:i+=1
print(i)
