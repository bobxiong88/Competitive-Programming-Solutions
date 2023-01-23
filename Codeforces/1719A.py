import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int,input().split())
    res = ((n%2)^1+1)+((m%2)^1+1)
    if res%2:
        print("Burenka")
    else:
        print("Tonya")
    
