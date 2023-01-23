lis=[]
store=[[2,"a","b","c"],[3,"d","e","f"],[4,"g","h","i"],[5,"j","k","l"],[6,"m","n","o"],[7,"p","q","r","s"],[8,"t","u","v"],[9,"w","x","y","z"]]
while True:
    num=33333333
    click=0
    total=0
    inp=input()
    if inp=="halt":
        break
    for l in inp:
        for i in store:
            click=0
            bignut=False
            for x in i: 
                if l==x:
                    bignut=True
                    if num==i[0]:
                        total+=2
                    num=i[0]
                    break
                click+=1
            if bignut==True:
                total+=click
                break
    lis.append(total)
for i in lis:
    print(i)