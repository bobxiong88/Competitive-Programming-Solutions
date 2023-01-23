import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    
    print(b,min(c,max(b,c-b+1)),c)
    
