a = int(input())
b = int(input())
c = 0
for x in range(a, b+1):
    f = 0
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            f+=2
            if i*i==x: f-=1
    if f==4: c+=1
print("The number of RSA numbers between {} and {} is {}".format(a,b,c))