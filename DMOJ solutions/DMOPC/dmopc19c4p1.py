strings=[]
num=["0","1","2","3","4","5","6","7","8","9","(",")",""]
for i in range(int(input())):
    strings.append(input())





for string in strings:


    
    op=0
    cl=0
    valid=True

    for position,character in enumerate(string):
        if character=="(":
            op+=1
        elif character==")":
            cl+=1
        elif character not in num:
            valid=False              
                    
    if string[0]==")" or string[-1]=="(":
        valid=False

    lis=[]
    for position,character in enumerate(string):
        if character=="(":
            len_before=len(lis)
            for p,c in enumerate(string):
                if p>position:
                    if c==")" and (p not in lis):
                        lis.append(p)
                        break

            if len_before==len(lis):
                valid=False
 


    
    if op!=cl:
        valid=False
    if string=="":
        valid=True
    if valid==True:
        print("YES")
    else:
        print("NO")