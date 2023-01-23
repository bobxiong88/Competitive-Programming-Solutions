def solve(n,k): 
    
    if (n >= (k**2)):
        nState = n%2 == 0
        kState = k%2 == 0
        if nState == kState:
            
            return "YES"
  
    return "NO"

N = int(input())

for i in range(N):
    n, k = [int(i) for i in input().split()]
    print(solve(n,k))
