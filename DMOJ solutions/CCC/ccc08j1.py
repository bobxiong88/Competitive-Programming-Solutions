weight = float(input())
height = float(input())
bmi = weight / (height)**2
if bmi<18.5:
    print("Underweight")
elif bmi>= 18.5 and bmi<=25:
    print("Normal weight")
else:
    print("Overweight")