import sys
input = sys.stdin.readline
a,b = map(int,input().split())
print(pow(2, (a-1)*(b-1), int(1e9)+7))