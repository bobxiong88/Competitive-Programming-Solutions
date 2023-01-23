N = {0:0,
     1:1,
     8:8,
     6:9,
     9:6}
m = int(input())
n = int(input())
count = 0
for num in range(m,n+1):
    num = list(str(num))
    yes = True
    for i in num:
        if int(i) not in N:
            yes = False
            break
    if not yes:
        continue

    newNum = [str(N[int(i)]) for i in list(reversed(num))]
    if num == newNum:
        count+=1
print(count)