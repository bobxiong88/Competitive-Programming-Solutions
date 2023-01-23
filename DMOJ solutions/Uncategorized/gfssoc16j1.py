numCourse,numHas = [int(i) for i in input().split()]
total = []
for i in range(numCourse):
    course = input()
    if course == "Math":
        total.append(4)
    elif course == "Chemistry":
        total.append(3)
    elif course == "English":
        total.append(2)
    else: 
        total.append(1)

if sum(total)<=numHas:
    print("YEA BOI")
else:
    print("Go to Metro")
    totalNum = sum(total)
    total = sorted(total)
    courses=0
    for i in range(len(total)):
        numHas-=total[i]
        if numHas>=0:
            courses+=1
        else:
            break
    print(courses)