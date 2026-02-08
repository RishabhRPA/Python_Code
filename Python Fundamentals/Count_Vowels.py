input_Str=input("Please Enter a String:")
Count=0
lst_Wovels={"a","e","i","o","u","A","E","I","O","U"}
for eachCh in input_Str:
    if eachCh in lst_Wovels:
        Count=Count+1
print(Count)



