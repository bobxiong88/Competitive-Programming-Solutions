N = int(input())
a = int(input())
p=[]
for i in range(N-1):
    p.append(int(input()))
if a<=max(p):
    print("NO")
else:
    print("YES")