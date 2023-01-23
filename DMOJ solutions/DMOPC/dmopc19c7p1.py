a,b,c,d = map(int,input().split())
C = a + b + c + 1
H = d
if H!=2*C+2:
    print("invalid")
else:
    print("C"+str(C)+"H"+str(H))