getNum=int(input("Enter Number:"))
def getFact(Num):
    fact=1
    for i in range(1,Num+1):
        fact=fact*i
    return fact
print(getFact(getNum))
