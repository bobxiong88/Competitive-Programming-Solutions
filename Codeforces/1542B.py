import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, a, b = map(int,input().split())
    if a == 1:
        if (n-1)%b == 0: print("Yes")
        else: print("No")
    else:
        x = 1
        found = False
        while x <= n:
            if x%b == n%b:
                print("Yes")
                found = True
                break
            x *= a        
        if not found:
            print("No")
