a= int(input())
b= int(input())
c= int(input())

if (a+b+c)==180:
    if a!=b and b!=c and c!=a:
        print("Scalene")
    else:
        if a==b==c:
            print("Equilateral")
        else:
            print("Isosceles")
else:
    print("Error")