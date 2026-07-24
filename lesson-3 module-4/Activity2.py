# Initialize dictionary

test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("original dictonary ",test_dict)
k=2
count=0
for key in test_dict:
    if test_dict[key]==k:
        count=count+1
print("frequency of 2 is ",count)