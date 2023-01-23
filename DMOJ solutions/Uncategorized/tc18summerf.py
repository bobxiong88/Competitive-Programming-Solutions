import sys
input = sys.stdin.readline
S = int(input())
T = int(input())
print("S" if S>T else ("E" if S==T else "T"))