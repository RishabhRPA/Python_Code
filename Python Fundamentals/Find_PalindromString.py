str1=input("Please Enter a string to check Palindrome:")
if(str1.lower()==str1[::-1].lower()):
    print(f"String is Palindrome:{str1}")
else:
    print(f"String is not Palindrome:{str1}")
