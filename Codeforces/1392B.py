import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    mx = max(a)
    s1 = []
    for i in a: s1.append(mx-i)
    s2 = []
    mx = max(s1)
    for i in s1: s2.append(mx-i)
    if k%2==0:
        print(*s2)
    else:
        print(*s1)
        
