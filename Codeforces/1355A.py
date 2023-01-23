import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,k = map(int,input().split())
    for i in range(k-1):
        al = [int(i) for i in str(a)]
        a = a + min(al)*max(al)
        if min(al) == 0:
            break
    print(a)
