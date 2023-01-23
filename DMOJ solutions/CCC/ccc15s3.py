import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
gates = [0]*(G+1)
for i in range(P):
    p = int(input())
    while True:
        gates[p]+=1
        if gates[p]==1:
            break
        if gates[p]>p:
            print(i)
            sys.exit(0)
        p-=gates[p]
        p+=1
print(P)