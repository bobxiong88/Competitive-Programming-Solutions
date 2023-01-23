import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1,n//2+1):
        ans+=i**2*8
    print(ans)
            
