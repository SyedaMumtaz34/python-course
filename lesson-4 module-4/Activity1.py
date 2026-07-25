Basket_1={"Mango","Apple","orange","Banana","berry"}
Basket_2={"Kiwi","Strawberry","Grapes","Banana","berry"}
print("Basket_1: ",Basket_1)
print("Basket_2: ",Basket_2)

Basket_1.add("watermelon")
print("Basket_1 after adding watermelon ",Basket_1)

Common_fruit=Basket_1.intersection(Basket_2)
print("fruits in both basket ",Common_fruit)

#array 
import array as arr
fruit_count=arr.array('i',[3,5,2,4])
print("fruit_count array ",fruit_count)

fruit_count.insert(0,1)
fruit_count.append(6)
print("fruit_count after adding item: ",fruit_count)

count_4=fruit_count.count(4)
print("number of times 4 appears: ",count_4)

fruit_count.reverse()
print("reverse fruit_count: ",fruit_count)
