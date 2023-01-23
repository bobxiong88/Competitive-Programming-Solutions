import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,s = map(int,input().split())
    a = [int(i) for i in str(n)]
    cost = 0
    for i in range(-1,-len(a)-1,-1):
        if sum(a)<=s:
            break
        cost += (10-a[i])*(10**(abs(i)-1))
        n+=(10-a[i])*(10**(abs(i)-1))
        a = [int(i) for i in str(n)]
    print(cost)
        
    
        
