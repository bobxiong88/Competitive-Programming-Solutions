import sys
input = sys.stdin.readline
N = int(input())
a =[]
for i in range(N):
    a.append(input())
c = 0
for i in range(N):
    if a[i] == input():
        c+=1
print(c)