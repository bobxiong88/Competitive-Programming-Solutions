import sys
input = sys.stdin.readline
n = int(input())
a = int(input())
b = int(input())
c = int(input())
cnt = 0
while n!=0:
    if cnt%3 == 0:
        a+=1
        if a == 35:
            n += 30
            a = 0
    elif cnt%3 == 1:
        b+=1
        if b == 100:
            n += 60
            b = 0
    else:
        c+=1
        if c == 10:
            n += 9
            c = 0
    n-=1
    cnt+=1
print("Martha plays {} times before going broke.".format(cnt))