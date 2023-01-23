import sys
input = sys.stdin.readline
for i in range(5):
    a,b = map(int,input().split())
    c = 0
    for n in range(a, b+1):
        f = True
        arr = [int(i) for i in str(n)]
        if sum(arr)%2:
            f = False
            continue
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                f = False
                break
        if not f: continue
        for i in range(int(n**0.5), 1,-1):
            if not n%(i**2):
                f = False
                break
        if f: c+=1
    print(c)