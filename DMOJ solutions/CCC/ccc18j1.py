yes=True
number = []
for i in range(4):

    number.append(int(input()))

if (number[0] == 9 or number[0]==8)  and (number[-1] == 9 or number[-1]==8)and number[1]==number[2]:
    print("ignore")
else:
    print("answer")