import sys
input = sys.stdin.readline
def monkey(string):
    if string=="A":
        return True
    if len(string)>2:
        if string[0]=="B" and monkey(string[1:len(string)-1]) and string[-1]=="S":
            return True
    for i in range(len(string)):
        if string[i] == "N":
            if monkey(string[:i]) and monkey(string[i+1:]):
                return True
    return False
while True:
    word = input()
    word = list(word)
    word.pop()
    word = "".join(word)
    if word=="X":
        break
    if monkey(word):
        print("YES")
    else:
        print("NO")