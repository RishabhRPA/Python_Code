list1=[1,2,3,4,5,4,2,9,9,9]
duplicate_lst=[]
for i in range(len(list1)):
   for j in range(i+1,len(list1)):
     if list1[i]==list1[j] and list1[i] not in duplicate_lst:
       duplicate_lst.append(list1[i])

print(duplicate_lst)

      