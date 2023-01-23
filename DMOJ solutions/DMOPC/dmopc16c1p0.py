W = int(input())
C = int(input())
if W == 3 and C>=95:
    ans = 'absolutely'
elif W == 1 and C<=50:
    ans = 'fairly'
else:
    ans = 'very'
print("C.C. is {} satisfied with her pizza.".format(ans))