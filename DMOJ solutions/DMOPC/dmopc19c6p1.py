def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x

def trim(a):
    a = list(str(a))
    del a[-1]
    return "".join(a)
def standardForm(x1,y1,x2,y2):
    a = y1-y2
    b = x2-x1
    c = x1*y2-x2*y1
    gcd = find_gcd(a,b)
    gcd = find_gcd(gcd,c)
    if gcd ==0 :
        pass
    elif a>=0 and gcd>=0:
        pass
    elif (a>=0 and gcd<0) or (gcd>=0 and a<0):
        gcd = -gcd
    return a/gcd, b/gcd, c/gcd
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       pass

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def intersection(a,b,c,j,k,l):
    
    x = (c*k-b*l)/(b*j-a*k)
    y = (a*l-c*j)/(b*j-a*k)

    return x, y


x1,y1,x2,y2 = [int(i) for i in input().split()]

a1,b1,a2,b2 = [int(i) for i in input().split()]


a,b,c = standardForm(x1,y1,x2,y2)
d,e,f = standardForm(a1,b1,a2,b2)

if (a,b,c) == (d,e,f):
    print("coincident")
elif (a,b) == (d,e):
    print("parallel")
elif (b==0 and e==0):
    print("parallel")
elif b*d==a*e:
    print("coincident")
else:
    x,y = intersection(a,b,c,d,e,f)
    if x == 0:
        x = 0
    if y == 0:
        y = 0
    x = "{0:.7f}".format(x)
    y = "{0:.7f}".format(y)
    print(trim(x),trim(y))