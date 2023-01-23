T = input()
S = input()

shifts = [S]
length = len(S)
inString = False
if S in T:
    inString = True
if inString == False:
    
    for i in range(length-1):
        pre = shifts[i]
        newString = pre[1:length]+pre[0]
        shifts.append(newString)
        if newString in T:
            inString = True
            break

if inString ==True:
    print("yes")

else:
    print("no")