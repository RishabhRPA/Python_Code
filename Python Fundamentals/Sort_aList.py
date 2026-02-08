get_lst=[5,4,2,5,1,6]
for i in range(len(get_lst)):
    for j in range(i+1, len(get_lst)):
        if get_lst[i]>get_lst[j]:
            get_lst[i],get_lst[j]=get_lst[j],get_lst[i]

print("Second Largest Number is",get_lst[len(get_lst)-2])
print(get_lst)       