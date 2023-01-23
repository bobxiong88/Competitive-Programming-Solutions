import sys
input = sys.stdin.readline
cycles = []
while True:
    cycle = input()
    if cycle[0] == "0":
        break
    cycles.append(cycle)
poop=[]
for cycle in cycles:
    poop.append([int(i) for i in cycle.split()][1:])
cycles = poop
for cycle in cycles:
    differences = []
    for i in range(len(cycle)-1):
        differences.append(cycle[i+1] - cycle[i])

    
    nums = [int(i) for i in range(1,len(differences)+1)]
    printed = False
    for num in nums:
        

          
        cycle = differences[:num]
        cycler = True
        for i in range(int(len(differences)/num)):
            if differences[i*num:(i+1)*num] != cycle:
                cycler = False
                break
        if cycle[:len(differences)%num]!= differences[int(len(differences)/num)*num:]:
            cycler = False
        if cycler == True:
            print(len(cycle))
            printed = True
            break
        
    if printed == False:
        print(0)