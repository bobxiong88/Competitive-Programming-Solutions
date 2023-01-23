import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    piles = list(map(int,input().split()))
    k = 0
    cycle = True
    for i in piles:
        if i==1 and cycle:
            k+=1
        else:
            cycle = False
    if piles == [1]*n:
        if n%2==0:
            print('Second')
        else:
            print('First')
    else:
        if k%2==0:
            print('First')
        else:
            print('Second')
            
