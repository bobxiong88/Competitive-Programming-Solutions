import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = map(str,input().split())
    s = str(int(a[::-1])+int(b[::-1]))
    print(int(s[::-1]))