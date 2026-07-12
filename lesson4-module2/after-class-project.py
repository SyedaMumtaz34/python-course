products = int(input("Enter number of products: "))
boxes = int(input("Enter the number of boxes: "))
stock = []
Product = 1

while Product <= products:
    print("Product", Product)
    box = 1
    product_stock = []
    while box <= boxes:
        quantity = int(input("Enter the quantity in box: "))
        product_stock.append(quantity)
        print("Box", box, "contains", quantity, "items")
        box += 1
    stock.append(product_stock)
    Product += 1

print("====Final stock report====")
for product in range(products):
    print("Product", product+1)
    for box in range(boxes):
        print("Box", box+1, "contains", stock[product][box], "items")