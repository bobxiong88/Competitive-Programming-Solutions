print("Ready")
while True:
    s = input()
    if s.strip(' ').strip('\n') == '': break
    a = [{'b','d'},{'q','p'}]
    if set(s) in a:
        print("Mirrored pair")
    else:
        print("Ordinary pair")