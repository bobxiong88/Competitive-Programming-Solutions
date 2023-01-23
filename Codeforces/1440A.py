import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,c0,c1,h = map(int,input().split())
    b = input().strip('\n')
    z = b.count('0')
    o = b.count('1')
    ans = float('inf')
    s = 0
    for i in range(z+1):
        ans = min(ans, z*c0+o*c1+s)
        s += h
        z-=1
        o+=1
    s = 0
    z = b.count('0')
    o = b.count('1')
    for i in range(o+1):
        ans = min(ans, z*c0+o*c1+s)
        s += h
        z+=1
        o-=1
    print(ans)
        
