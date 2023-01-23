import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
print(max(a)-min(a))