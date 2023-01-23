import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    choices = []
    left = []
    princes = [False]*(n+1)
    for p in range(1,n+1):
        options = tuple(map(int,input().split()))
        found = False
        if options == (0):
            pass
        else:
            for i in range(1,options[0]+1):
                if not princes[options[i]]:
                    princes[options[i]] = True
                    found = True
                    break
        if not found:
            left.append(p)
    if not left:
        print("OPTIMAL")
        continue
    print("IMPROVE")
    for i in range(1,n+1):
        if not princes[i]:
            print(left[0], i)
            break
                
    
