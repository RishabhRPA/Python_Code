get_Input=input("Please Enter a String:")
print(get_Input[::-1])
rev_str=""
for i in get_Input:
    rev_str=i+rev_str
print(rev_str)