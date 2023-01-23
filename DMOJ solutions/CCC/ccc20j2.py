P = int(raw_input())
N = int(raw_input())
R = int(raw_input())

total = N
c=0
while total<=P:
    N*=R
    total+=N
    c+=1
print(c)