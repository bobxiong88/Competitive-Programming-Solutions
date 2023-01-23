import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s, x = input().split()
    x = int(x)
    h, m = map(int,s.split(':'))
    porn = (h,m)
    ans = 0
    while True:
        m += x
        h += m//60
        m %= 60
        h %= 24
        a,b = map(str,(h,m))
        if h < 10: a = '0'+a
        if m < 10: b = '0'+b
        if a+b==str(a+b)[::-1]: ans +=1
        if (h,m)==porn: break
        #print(porn,(h,m))
    print(ans)
