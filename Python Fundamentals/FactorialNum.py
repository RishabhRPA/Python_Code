input_num=int(input("Enter a number to find factorial:"))
factNo=1
while(input_num>=1):
    factNo=factNo*input_num
    input_num=input_num-1

print(f"Factorial Number is:{factNo}")
