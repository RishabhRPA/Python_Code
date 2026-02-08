
for i in range(7):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,7):
    space= " "*(2*(7-i))
    star="* " * i
    print(space + star)
