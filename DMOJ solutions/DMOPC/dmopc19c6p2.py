def cringe(gamer,key):
    count=0
    
    while True:
        gamer = gamer/key
        
        if int(gamer) != gamer:
            break
        
        count+=1
        
    return count

def primeFactors(n):
    factors = []
    while n % 2 == 0: 
        factors.append(2)
        n = n / 2
    for i in range(3,int(n**0.5)+1,2): 
        while n % i== 0: 
            factors.append(i)
            n = n / i 
    if n > 2: 
        factors.append(n)
    return factors
a, b = [int(i) for i in input().split()]

aFactors = primeFactors(a)
bFactors = primeFactors(b)

aGraph = {}  
bGraph = {}

for factor in aFactors:
    if factor not in aGraph.keys():
        aGraph.update({factor:1})
    else:
        aGraph[factor]+=1
        
m = 1000000000000000

for key in aGraph.keys():
    n=0
    
    for i in range(1,int(b//key + 1)):
        gamer = i*key
        n+=cringe(gamer,key)
        
    mininum = n//aGraph[key]
    
    if mininum<m:
        m = mininum

print(m)