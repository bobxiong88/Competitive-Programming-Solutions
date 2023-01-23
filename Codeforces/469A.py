import sys
input = sys.stdin.readline
n = int(input())
a = set(list(map(int,input().split()))[1:])
b = set(list(map(int,input().split()))[1:])
a=a.union(b)
if len(a) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
