def solve(Va,Vb,M,order):
    m=0
    n=0
    operations = []
    states = []
    while True:
        if m==M or n==M:
            return operations
        elif m==0:
            m+=Va
            states.append((m,n))
            
            operations.append(str("fill "+order[0]))
        elif n==Vb:
            n=0
            states.append((m,n))
            operations.append(str("chug "+ order[1]))
        else:
            difference = Vb-n
            if difference > m:
                n+=m
                m=0
            else:
                n = Vb
                m-=difference
            states.append((m,n))
            operations.append(str("pour "+order[0]+" "+order[1]))
        if states[-1] in states[:len(states)-1]:
            return False
        
            
            
            

Va,Vb,M = map(int,raw_input().split())
one = solve(Va,Vb,M,["A","B"])
two = solve(Vb,Va,M,["B","A"])
if not one and not two:
    print("Not possible")
else:
    if len(one)<=len(two):
        for i in one:
            print(i)
    else:
        for i in two:
            print(i)