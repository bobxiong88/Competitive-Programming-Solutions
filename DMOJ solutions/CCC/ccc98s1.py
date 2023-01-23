n = int(input())
for _ in range(n):
    sentence = input().split()
    for p,word in enumerate(sentence):
        if len(word)==4:
            sentence[p]="****"
    print(" ".join(sentence))