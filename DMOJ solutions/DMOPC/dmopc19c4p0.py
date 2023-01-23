A=input()
B=input()

c=0
for i in range(len(A)):
    if A[i]!=B[i]:
        c+=1

if c==1:
    print("LARRY IS SAVED!")
else:
    print("LARRY IS DEAD!")