month = int(input())
day = int(input())

if month == 2:
    if day < 18:
        print("Before")
    elif day >18 :
        print("After")
    else:
        print("Special")
else:
    if month<2:
        print("Before")
    else:
        print("After")