x = int(input())
y = int(input())
k = (x*y)%4
a = ['.00', '.25', '.50', '.75']
print(str(x*y//4)+a[k])