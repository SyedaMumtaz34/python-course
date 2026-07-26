items=["pencil","eraser","Notebook","sharpner","glue"]
stock_count=[12,0,8,5,3]
inventory={item:count for item,count in zip(items,stock_count)}
print("full inventory",inventory)

in_stock_item=[item for item in items if inventory[item]>0]
print("item in stock",in_stock_item)

chosen_item=input("which item do you want to buy?")
if chosen_item not in inventory or inventory[chosen_item]==0:
    print(chosen_item,"is out of stock! stopping the cheacker")
    exit()

prices=[10,5,40,15,20]
mark_up=int(input("enter a mark_up amount to add to every price: "))

mark_up_price=list(map(lambda p:p + mark_up,prices))
print("mark_up_price",mark_up_price)

item_index=items.index(chosen_item)
chosen_price=mark_up_price[item_index]
print("price of ",chosen_item,"after mark_up",chosen_price)

inventory[chosen_item]=inventory[chosen_item]-1
print(chosen_item,"perchased! remaining stock: ",inventory[chosen_item])