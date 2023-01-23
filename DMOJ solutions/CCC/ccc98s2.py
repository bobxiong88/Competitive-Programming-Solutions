def findSum(num):
    s = 1
    i = 2
    while i<=(num**0.5):
        if (num%i==0):
            if (i==(num/i)):
                s+=i
            else:
                s+=i+(num/i)
        i+=1
    return s
def digitSum(num):
    num = str(num)
    s=0
    for i in num:
        s+=int(i)**3
    return s
perfect = []
for i in range(1000,10000):
    if findSum(i)==i:
        perfect.append(str(i))

print(" ".join(perfect))
cube = []
for i in range(100,1000):
    if digitSum(i)==i:
        cube.append(str(i))
print(" ".join(cube))