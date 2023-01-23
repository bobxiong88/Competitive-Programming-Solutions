import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
left = [0]*N
right = [0]*N
p1 = [0]*N
p2 = [0]*N
for i in range(N):
    if i:
        left[i] = abs(a[i]-a[i-1])+left[i-1]
for i in range(N-1,-1,-1):
    p1[i] = left[i]
    if i != N-1:
        p1[i] += p1[i+1]
for i in range(N-1,-1,-1):
    if i!=N-1:
        right[i] = abs(a[i]-a[i+1])+right[i+1]
for i in range(N):
    p2[i] = right[i]
    if i:
        p2[i] += p2[i-1]
for i in range(int(input())):
    h = int(input())
    h -= 1
    l = 0
    r = 0
    l = p1[h]-(N-h)*left[h]
    if h: r = p2[h-1]-h*right[h]
    print(l+r)