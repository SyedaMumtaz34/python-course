l_list=[4,5,1,2,9,7,10,8]
print("original list ",l_list)

count=0
for i in l_list:
    count+=i
print("Sum= ",count)
avg=count/len(l_list)
print("avg= ",avg)

l_list.sort()
print("sorted list ",l_list)
print("first element of my sorted list is ",l_list[0])
print("last element of my sorted list is ",l_list[-1])