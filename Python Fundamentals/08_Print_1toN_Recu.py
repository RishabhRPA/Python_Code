def print_Num(n):
    if (n==0):
        print(n)
    else:
       
         print_Num(n-1)
         print(n)

print_Num(8)       