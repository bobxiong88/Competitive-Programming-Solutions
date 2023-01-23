import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = (1+(1+8*k)**0.5)/2
    if int(a) == a:
        a = int(a)
        print('a'*(n-a)+'bb'+'a'*(a-2))
        continue
    a = int(a)
    p = int(a*(a+1)/2)
    c = int(a*(a-1)/2)
    print('a'*(n-(a+1))+'b'+'a'*(p-k)+'b'+'a'*(k-c-1))

    
