year=int(input())


while True:
    year+=1

    str_year=str(year)
    distinct=True
    for p,c in enumerate(str_year):
        for character in str_year[p+1:]:
            if c==character:
                distinct=False
                break
        if distinct==False:
            break
    if distinct==True:
        print(year)
        break