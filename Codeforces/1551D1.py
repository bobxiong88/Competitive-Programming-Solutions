import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, k = map(int,input().split())
    h = k
    v = (n*m)//2-k
    if m%2 == 0:
        four = (m//2)*(n//2)
        #print(1,four)
        if v%2 == 0 and v//2 <= four:
            print("YES")
        else:
            print("NO")
    else:
        four = (m//2)*(n//2)
       # print(2, four)
        if h%2 == 0 and h//2 <= four:
            print("YES")
        else:
            print("NO")
