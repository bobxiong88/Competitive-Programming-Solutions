s=0
burger=int(input(""))
side=int(input(""))
drink=int(input(""))
dessert=int(input(""))

if burger==1:
    s+=461
elif burger==2:
    s+=431
elif burger==3:
    s+=420

if side==1:
    s+=100
elif side==2:
    s+=57
elif side==3:
    s+=70

if drink==1:
    s+=130
elif drink==2:
    s+=160
elif drink==3:
    s+=118

if dessert==1:
    s+=167
elif dessert==2:
    s+=266
elif dessert==3:
    s+=75
print("Your total Calorie count is",str(s)+".")