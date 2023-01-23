A = 0
B = 0

high = ["","jack", "queen", "king", "ace"]


Acard = 0
Bcard = 0

Acounter = 0
Bcounter = 0
for i in range(52):

    card = input()
    if card in high:
        if Acard!=0:
            Acard = 0
            Acounter = 0
        if Bcard!=0:
            Bcard = 0
            Bcounter = 0
        
    if Acard!=0:
        Acounter+=1
    if Bcard!=0:
        Bcounter+=1

    if Acard == Acounter !=0 :
        print("Player A scores",Acard,"point(s).")
        A+=Acard
        Acard = 0
        Acounter = 0
        
    if Bcard == Bcounter != 0:
        print("Player B scores",Bcard,"point(s).")
        B+=Bcard
        Bcard = 0
        Bcounter = 0
        
    if card in high:
        

            
        if i%2 == 0 :
            Acard = high.index(card)
            Acounter = 0
        else:
            Bcounter = 0
            Bcard = high.index(card)
        
        
    
print("Player A:",A,"point(s).")
print("Player B:",B,"point(s).")