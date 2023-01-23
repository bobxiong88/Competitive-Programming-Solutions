import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    out=[]
    n = str(n)
    for i in range(len(n)):
        if n[i]!='0':
            out.append(n[i]+'0'*(len(n)-i-1))
    print(len(out))
    print(*out)
            
