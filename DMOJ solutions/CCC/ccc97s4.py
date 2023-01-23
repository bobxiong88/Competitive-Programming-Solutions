t = int(input())

for case in range(t):
    dictionary = {}
    

    c=0

    while True:
        new = []
        line = input()
        if line == "":
            break
        line = line.split()
        for word in line:
           
           if word not in dictionary.keys():
               c+=1
               dictionary.update({word:c})
               new.append(word)
           else:
               new.append(str(dictionary[word]))
        print(" ".join(new))
    print()