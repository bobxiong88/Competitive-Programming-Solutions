lis1=[]
lis2=[]
first=input()
second=input()
for i in first:
    if i!=" ":
        lis1.append(i)
for i in second:
    if i!=" ":
        lis2.append(i)
lis1.sort()
lis2.sort()
if lis1==lis2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")