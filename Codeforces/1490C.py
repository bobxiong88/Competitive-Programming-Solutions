import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())
    num = set()
    for i in range(1,int(x**(1/3))+3):
        num.add(i**3)
    #print(len(num))
    ans = 'NO'
    for i in num:
        if x-i in num:
            ans = 'YES'
            break
    print(ans)
