T = int(input())
C = int(input())
a = [int(input()) for i in range(C)]
a.sort()
s = 0
for i in range(C):
    s += a[i]
    if s > T:
        break
print(i+int(s<=T))