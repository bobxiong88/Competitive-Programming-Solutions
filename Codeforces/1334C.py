import sys
input = sys.stdin.buffer.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a,b = [],[]
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        b[i] = min(a[(i+1)%n],b[i])
    b[-1] = min(a[0],b[-1])
    print(sum(a)-sum(b)+min(b))
        
        
